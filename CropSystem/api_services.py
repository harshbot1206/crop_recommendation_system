import requests
import json
from datetime import datetime, timedelta
import logging
from .config import Config
from .api_endpoints import SOIL_API_CONFIG, MANDI_API_CONFIG

logger = logging.getLogger(__name__)

class APIService:
    def __init__(self):
        # Load configuration
        self.config = Config()
        
        # API Keys from configuration
        self.weather_api_key = self.config.OPENWEATHER_API_KEY
        self.soil_api_key = self.config.SOIL_API_KEY
        self.mandi_api_key = self.config.MANDI_API_KEY
        self.mandi_api_url = self.config.MANDI_API_URL
        
    def get_weather_data(self, location):
        """Fetch weather data from OpenWeatherMap API for Gujarat locations"""
        try:
            if self.weather_api_key == 'YOUR_OPENWEATHER_API_KEY':
                logger.warning("OpenWeatherMap API key not configured")
                return self._get_gujarat_sample_weather_data(location)
                
            url = f"http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': f"{location},IN",  # India
                'appid': self.weather_api_key,
                'units': 'metric'
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            # Get rainfall data - try multiple sources
            rainfall = 0
            if 'rain' in data and '1h' in data['rain']:
                rainfall = data['rain']['1h']
            elif 'rain' in data and '3h' in data['rain']:
                rainfall = data['rain']['3h']
            elif 'rain' in data and '24h' in data['rain']:
                rainfall = data['rain']['24h']
            
            # If no rain data, check if it's currently raining
            if rainfall == 0 and 'weather' in data:
                weather_desc = data['weather'][0]['description'].lower()
                if any(word in weather_desc for word in ['rain', 'drizzle', 'shower']):
                    rainfall = 0.5  # Light rain if weather description indicates rain
            
            return {
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'rainfall': rainfall,
                'description': data['weather'][0]['description']
            }
        except Exception as e:
            logger.error(f"Error fetching weather data: {e}")
            return self._get_gujarat_sample_weather_data(location)
    
    def get_soil_data(self, lat, lon):
        """Fetch soil data using the user's soil API key"""
        try:
            # Use the user's soil API with the provided key
            soil_api_endpoint = f"{SOIL_API_CONFIG['base_url']}{SOIL_API_CONFIG['endpoint']}"
            
            headers = {
                'Authorization': f"{SOIL_API_CONFIG['auth_type']} {self.soil_api_key}",
                'Content-Type': 'application/json'
            }
            
            params = {
                'lat': lat,
                'lon': lon,
                'format': 'json'
            }
            
            logger.info(f"Fetching soil data from: {soil_api_endpoint}")
            response = requests.get(soil_api_endpoint, headers=headers, params=params, timeout=15)
            
            if response.status_code == 200:
                data = response.json()
                soil_data = {
                    'N': data.get('nitrogen', 75.0),
                    'P': data.get('phosphorus', 35.0),
                    'K': data.get('potassium', 180.0),
                    'ph': data.get('ph', 7.2),
                    'organic_carbon': data.get('organic_carbon', 37.5),
                    'soil_type': data.get('soil_type', 'Gujarat soil'),
                    'source': 'Real API'
                }
                logger.info("Successfully fetched soil data from API")
                return soil_data
            else:
                logger.warning(f"Soil API returned status {response.status_code}")
                # Return sample data as fallback
                return self._get_gujarat_sample_soil_data(lat, lon)
                
        except Exception as e:
            logger.error(f"Error fetching soil data: {e}")
            # Return sample data as fallback
            return self._get_gujarat_sample_soil_data(lat, lon)
    
    def get_location_coordinates(self, location):
        """Get coordinates for Gujarat locations"""
        try:
            if self.weather_api_key == 'YOUR_OPENWEATHER_API_KEY':
                logger.warning("OpenWeatherMap API key not configured")
                return self._get_gujarat_coordinates(location)
                
            url = f"http://api.openweathermap.org/geo/1.0/direct"
            params = {
                'q': f"{location},IN",
                'limit': 1,
                'appid': self.weather_api_key
            }
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            if data:
                return {
                    'lat': data[0]['lat'],
                    'lon': data[0]['lon']
                }
            return None
        except Exception as e:
            logger.error(f"Error fetching coordinates: {e}")
            return self._get_gujarat_coordinates(location)
    
    def get_mandi_prices(self, crop_name):
        """Fetch mandi prices using the user's mandi API key"""
        try:
            # Use the user's mandi API with the provided key
            mandi_api_endpoint = f"{MANDI_API_CONFIG['base_url']}{MANDI_API_CONFIG['endpoint']}"
            
            headers = {
                'Authorization': f"{MANDI_API_CONFIG['auth_type']} {self.mandi_api_key}",
                'Content-Type': 'application/json'
            }
            
            params = {
                'crop': crop_name.lower(),
                'region': 'gujarat'
            }
            
            logger.info(f"Fetching mandi prices from: {mandi_api_endpoint}")
            response = requests.get(mandi_api_endpoint, headers=headers, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                result = {
                    'crop': crop_name,
                    'price_per_quintal': data.get('price', 2500),
                    'market': data.get('market', 'Gujarat APMC Market'),
                    'date': data.get('date', datetime.now().strftime('%Y-%m-%d')),
                    'region': 'Gujarat, India',
                    'notes': 'Real-time data from API',
                    'source': 'Real API'
                }
                logger.info(f"Successfully fetched mandi prices for {crop_name}")
                return result
            else:
                logger.warning(f"Mandi API returned status {response.status_code}")
                # Return sample data as fallback
                return self._get_gujarat_mandi_prices(crop_name)
                
        except Exception as e:
            logger.error(f"Error fetching mandi prices: {e}")
            # Return sample data as fallback
            return self._get_gujarat_mandi_prices(crop_name)
    
    def get_planting_harvest_times(self, crop_name, location):
        """Get optimal planting and harvest times for Gujarat"""
        try:
            # Gujarat-specific crop calendar based on local agricultural practices
            gujarat_crop_calendar = {
                'cotton': {
                    'planting_start': 'May',
                    'planting_end': 'June',
                    'harvest_start': 'October',
                    'harvest_end': 'November',
                    'gujarat_notes': 'Major crop in Saurashtra and North Gujarat'
                },
                'groundnut': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Important oilseed crop in Saurashtra'
                },
                'wheat': {
                    'planting_start': 'November',
                    'planting_end': 'December',
                    'harvest_start': 'March',
                    'harvest_end': 'April',
                    'gujarat_notes': 'Rabi crop in North and Central Gujarat'
                },
                'rice': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'October',
                    'harvest_end': 'November',
                    'gujarat_notes': 'Kharif crop in South Gujarat'
                },
                'maize': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Popular in Central Gujarat'
                },
                'sugarcane': {
                    'planting_start': 'February',
                    'planting_end': 'March',
                    'harvest_start': 'December',
                    'harvest_end': 'March',
                    'gujarat_notes': 'Major crop in South Gujarat'
                },
                'pulses': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Various pulses grown across Gujarat'
                },
                'oilseeds': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Sesame, mustard, and other oilseeds'
                },
                'vegetables': {
                    'planting_start': 'Year-round',
                    'planting_end': 'Year-round',
                    'harvest_start': 'Year-round',
                    'harvest_end': 'Year-round',
                    'gujarat_notes': 'Tomatoes, onions, potatoes, etc.'
                },
                'muskmelon': {
                    'planting_start': 'February',
                    'planting_end': 'March',
                    'harvest_start': 'May',
                    'harvest_end': 'June',
                    'gujarat_notes': 'Summer fruit crop, popular in North and Central Gujarat'
                },
                'watermelon': {
                    'planting_start': 'January',
                    'planting_end': 'February',
                    'harvest_start': 'April',
                    'harvest_end': 'May',
                    'gujarat_notes': 'Summer fruit crop, grown across Gujarat'
                },
                'cucumber': {
                    'planting_start': 'February',
                    'planting_end': 'March',
                    'harvest_start': 'April',
                    'harvest_end': 'May',
                    'gujarat_notes': 'Summer vegetable crop'
                },
                'tomato': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Kharif vegetable crop, also grown in winter'
                },
                'onion': {
                    'planting_start': 'May',
                    'planting_end': 'June',
                    'harvest_start': 'August',
                    'harvest_end': 'September',
                    'gujarat_notes': 'Important vegetable crop in Gujarat'
                },
                'potato': {
                    'planting_start': 'October',
                    'planting_end': 'November',
                    'harvest_start': 'January',
                    'harvest_end': 'February',
                    'gujarat_notes': 'Rabi vegetable crop'
                },
                'chilli': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Spice crop, popular in Saurashtra'
                },
                'sesame': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Oilseed crop, major in Saurashtra'
                },
                'mustard': {
                    'planting_start': 'October',
                    'planting_end': 'November',
                    'harvest_start': 'February',
                    'harvest_end': 'March',
                    'gujarat_notes': 'Rabi oilseed crop'
                },
                'bajra': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Millet crop, drought-resistant'
                },
                'jowar': {
                    'planting_start': 'June',
                    'planting_end': 'July',
                    'harvest_start': 'September',
                    'harvest_end': 'October',
                    'gujarat_notes': 'Sorghum crop, grown in dry areas'
                }
            }
            
            return gujarat_crop_calendar.get(crop_name.lower(), {
                'planting_start': 'Varies by region',
                'planting_end': 'Varies by region',
                'harvest_start': 'Varies by region',
                'harvest_end': 'Varies by region',
                'gujarat_notes': 'Check with local agricultural extension office'
            })
        except Exception as e:
            logger.error(f"Error getting planting/harvest times: {e}")
            return None

    # Gujarat-specific sample data methods
    def _get_gujarat_sample_weather_data(self, location):
        """Return sample weather data for Gujarat cities"""
        gujarat_weather = {
            'ahmedabad': {'temperature': 32.5, 'humidity': 45.0, 'rainfall': 0.0, 'description': 'sunny'},
            'surat': {'temperature': 30.2, 'humidity': 65.0, 'rainfall': 2.5, 'description': 'partly cloudy'},
            'vadodara': {'temperature': 31.8, 'humidity': 50.0, 'rainfall': 0.0, 'description': 'clear sky'},
            'rajkot': {'temperature': 33.1, 'humidity': 40.0, 'rainfall': 0.0, 'description': 'sunny'},
            'bhavnagar': {'temperature': 29.5, 'humidity': 70.0, 'rainfall': 5.0, 'description': 'light rain'},
            'jamnagar': {'temperature': 32.0, 'humidity': 55.0, 'rainfall': 0.0, 'description': 'clear sky'},
            'anand': {'temperature': 30.5, 'humidity': 60.0, 'rainfall': 1.0, 'description': 'partly cloudy'},
            'mehsana': {'temperature': 34.2, 'humidity': 35.0, 'rainfall': 0.0, 'description': 'sunny'}
        }
        
        location_lower = location.lower()
        for city, weather in gujarat_weather.items():
            if city in location_lower:
                return weather
        
        # Default Gujarat weather
        return {'temperature': 31.0, 'humidity': 55.0, 'rainfall': 1.0, 'description': 'typical gujarat weather'}
    
    def _get_gujarat_sample_soil_data(self, lat, lon):
        """Return sample soil data for Gujarat regions"""
        # Gujarat has diverse soil types: Black soil (North), Red soil (Saurashtra), Alluvial soil (South)
        return {
            'N': 75.0,  # Medium nitrogen content
            'P': 35.0,  # Low to medium phosphorus
            'K': 180.0, # High potassium (typical of Gujarat soils)
            'ph': 7.2,  # Slightly alkaline (typical of Gujarat)
            'organic_carbon': 37.5,
            'soil_type': 'Black soil (North Gujarat) / Red soil (Saurashtra) / Alluvial (South Gujarat)',
            'source': 'Sample data'
        }
    
    def _get_gujarat_coordinates(self, location):
        """Return coordinates for major Gujarat cities"""
        gujarat_cities = {
            'ahmedabad': {'lat': 23.0225, 'lon': 72.5714},
            'surat': {'lat': 21.1702, 'lon': 72.8311},
            'vadodara': {'lat': 22.3072, 'lon': 73.1812},
            'rajkot': {'lat': 22.3039, 'lon': 70.8022},
            'bhavnagar': {'lat': 21.7645, 'lon': 72.1519},
            'jamnagar': {'lat': 22.4707, 'lon': 70.0737},
            'anand': {'lat': 22.5607, 'lon': 72.9628},
            'mehsana': {'lat': 23.5986, 'lon': 72.3764},
            'gandhinagar': {'lat': 23.2156, 'lon': 72.6369},
            'bharuch': {'lat': 21.6948, 'lon': 72.9805},
            'nadiad': {'lat': 22.6939, 'lon': 72.8616},
            'patan': {'lat': 23.8507, 'lon': 72.1147}
        }
        
        location_lower = location.lower()
        for city, coords in gujarat_cities.items():
            if city in location_lower:
                return coords
        
        # Default to Ahmedabad coordinates
        return {'lat': 23.0225, 'lon': 72.5714}
    
    def _get_gujarat_mandi_prices(self, crop_name):
        """Return sample mandi prices for Gujarat markets"""
        # Gujarat mandi prices (approximate, based on recent trends)
        gujarat_crop_prices = {
            'cotton': 6500,      # Major crop in Gujarat
            'groundnut': 5200,   # Important oilseed
            'wheat': 2200,       # Rabi crop
            'rice': 2800,        # Kharif crop
            'maize': 1800,       # Popular in Central Gujarat
            'sugarcane': 320,    # Major crop in South Gujarat
            'pulses': 4500,      # Various pulses
            'oilseeds': 3800,    # Sesame, mustard, etc.
            'vegetables': 1500,  # Tomatoes, onions, etc.
            'fruits': 2800,      # Mangoes, bananas, etc.
            'muskmelon': 1800,   # Summer fruit
            'watermelon': 1200,  # Summer fruit
            'cucumber': 800,     # Summer vegetable
            'tomato': 1200,      # Important vegetable
            'onion': 1000,       # Important vegetable
            'potato': 1400,      # Rabi vegetable
            'chilli': 8000,      # Spice crop
            'sesame': 4500,      # Oilseed
            'mustard': 4200,     # Oilseed
            'bajra': 1600,       # Millet
            'jowar': 1400        # Sorghum
        }
        
        price = gujarat_crop_prices.get(crop_name.lower(), 2500)
        
        # Major Gujarat mandis
        gujarat_mandis = [
            'APMC Ahmedabad', 'APMC Surat', 'APMC Vadodara', 
            'APMC Rajkot', 'APMC Bhavnagar', 'APMC Jamnagar',
            'APMC Anand', 'APMC Mehsana', 'APMC Gandhinagar'
        ]
        
        return {
            'crop': crop_name,
            'price_per_quintal': price,
            'market': 'Gujarat APMC Market',
            'date': datetime.now().strftime('%Y-%m-%d'),
            'region': 'Gujarat, India',
            'notes': 'Prices may vary by mandi and season',
            'source': 'Sample data'
        }

# Global API service instance
api_service = APIService()
