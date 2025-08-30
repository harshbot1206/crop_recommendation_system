"""
API Endpoints Configuration for Gujarat Crop Recommendation System
Replace these placeholder URLs with your actual API endpoints
"""

# Soil API Configuration
SOIL_API_CONFIG = {
    'base_url': 'https://api.soilservice.com',  # Replace with your actual soil API URL
    'endpoint': '/soil-data',  # Replace with your actual endpoint
    'method': 'GET',
    'auth_type': 'Bearer',  # or 'API-Key', 'Basic', etc.
    'parameters': {
        'lat': 'latitude',
        'lon': 'longitude',
        'format': 'json'
    }
}

# Mandi Price API Configuration
MANDI_API_CONFIG = {
    'base_url': 'https://api.mandiprices.com',  # Replace with your actual mandi API URL
    'endpoint': '/prices',  # Replace with your actual endpoint
    'method': 'GET',
    'auth_type': 'Bearer',  # or 'API-Key', 'Basic', etc.
    'parameters': {
        'crop': 'crop_name',
        'region': 'gujarat'
    }
}

# Example API endpoints (replace with your actual ones):
# SOIL_API_CONFIG['base_url'] = 'https://your-soil-api.com'
# MANDI_API_CONFIG['base_url'] = 'https://your-mandi-api.com'

# To use these endpoints, update the base_url in each config above
