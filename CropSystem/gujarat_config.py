"""
Gujarat-specific configuration for the Crop Recommendation System
"""

# Gujarat Agricultural Regions
GUJARAT_REGIONS = {
    'north_gujarat': {
        'districts': ['Ahmedabad', 'Gandhinagar', 'Mehsana', 'Patan', 'Banaskantha', 'Sabarkantha', 'Aravalli'],
        'soil_type': 'Black soil (Regur)',
        'major_crops': ['Cotton', 'Wheat', 'Maize', 'Pulses'],
        'climate': 'Semi-arid',
        'rainfall': '600-800 mm annually'
    },
    'saurashtra': {
        'districts': ['Rajkot', 'Jamnagar', 'Bhavnagar', 'Amreli', 'Junagadh', 'Porbandar', 'Devbhoomi Dwarka', 'Gir Somnath', 'Botad'],
        'soil_type': 'Red soil and Black soil',
        'major_crops': ['Groundnut', 'Cotton', 'Wheat', 'Oilseeds'],
        'climate': 'Semi-arid to arid',
        'rainfall': '500-700 mm annually'
    },
    'south_gujarat': {
        'districts': ['Surat', 'Valsad', 'Navsari', 'Bharuch', 'Narmada', 'Tapi', 'Dang'],
        'soil_type': 'Alluvial soil',
        'major_crops': ['Rice', 'Sugarcane', 'Vegetables', 'Fruits'],
        'climate': 'Humid subtropical',
        'rainfall': '1000-1500 mm annually'
    },
    'central_gujarat': {
        'districts': ['Vadodara', 'Anand', 'Kheda', 'Panchmahal', 'Dahod', 'Mahisagar', 'Chhota Udaipur'],
        'soil_type': 'Mixed soil types',
        'major_crops': ['Maize', 'Cotton', 'Wheat', 'Pulses'],
        'climate': 'Semi-arid',
        'rainfall': '700-900 mm annually'
    }
}

# Gujarat Major Crops with Details
GUJARAT_CROPS = {
    'cotton': {
        'gujarati_name': 'કપાસ',
        'regions': ['north_gujarat', 'saurashtra', 'central_gujarat'],
        'season': 'Kharif',
        'planting_months': ['May', 'June'],
        'harvest_months': ['October', 'November'],
        'soil_preference': 'Black soil, well-drained',
        'water_requirement': 'Medium',
        'major_districts': ['Ahmedabad', 'Rajkot', 'Vadodara', 'Mehsana']
    },
    'groundnut': {
        'gujarati_name': 'શેંગડા',
        'regions': ['saurashtra'],
        'season': 'Kharif',
        'planting_months': ['June', 'July'],
        'harvest_months': ['September', 'October'],
        'soil_preference': 'Sandy loam, well-drained',
        'water_requirement': 'Low to medium',
        'major_districts': ['Rajkot', 'Jamnagar', 'Amreli', 'Junagadh']
    },
    'wheat': {
        'gujarati_name': 'ઘઉં',
        'regions': ['north_gujarat', 'central_gujarat'],
        'season': 'Rabi',
        'planting_months': ['November', 'December'],
        'harvest_months': ['March', 'April'],
        'soil_preference': 'Clay loam, fertile',
        'water_requirement': 'Medium',
        'major_districts': ['Ahmedabad', 'Mehsana', 'Vadodara', 'Anand']
    },
    'rice': {
        'gujarati_name': 'ચોખા',
        'regions': ['south_gujarat'],
        'season': 'Kharif',
        'planting_months': ['June', 'July'],
        'harvest_months': ['October', 'November'],
        'soil_preference': 'Clay loam, water-retaining',
        'water_requirement': 'High',
        'major_districts': ['Surat', 'Valsad', 'Navsari', 'Bharuch']
    },
    'maize': {
        'gujarati_name': 'મકાઈ',
        'regions': ['central_gujarat', 'north_gujarat'],
        'season': 'Kharif',
        'planting_months': ['June', 'July'],
        'harvest_months': ['September', 'October'],
        'soil_preference': 'Loamy soil, fertile',
        'water_requirement': 'Medium',
        'major_districts': ['Vadodara', 'Anand', 'Ahmedabad', 'Mehsana']
    },
    'sugarcane': {
        'gujarati_name': 'શેરડી',
        'regions': ['south_gujarat'],
        'season': 'Year-round',
        'planting_months': ['February', 'March'],
        'harvest_months': ['December', 'March'],
        'soil_preference': 'Deep alluvial soil',
        'water_requirement': 'High',
        'major_districts': ['Surat', 'Bharuch', 'Valsad', 'Navsari']
    }
}

# Gujarat APMC Markets
GUJARAT_APMC_MARKETS = {
    'ahmedabad': {
        'name': 'APMC Ahmedabad',
        'address': 'Vasna, Ahmedabad',
        'contact': '+91-79-26602444',
        'major_crops': ['Cotton', 'Wheat', 'Vegetables', 'Fruits']
    },
    'surat': {
        'name': 'APMC Surat',
        'address': 'Udhna, Surat',
        'contact': '+91-261-2871234',
        'major_crops': ['Rice', 'Sugarcane', 'Vegetables', 'Fruits']
    },
    'vadodara': {
        'name': 'APMC Vadodara',
        'address': 'Makarpura, Vadodara',
        'contact': '+91-265-2641234',
        'major_crops': ['Maize', 'Cotton', 'Wheat', 'Pulses']
    },
    'rajkot': {
        'name': 'APMC Rajkot',
        'address': 'Race Course, Rajkot',
        'contact': '+91-281-2234567',
        'major_crops': ['Groundnut', 'Cotton', 'Oilseeds', 'Wheat']
    },
    'bhavnagar': {
        'name': 'APMC Bhavnagar',
        'address': 'Ghogha Road, Bhavnagar',
        'contact': '+91-278-2245678',
        'major_crops': ['Groundnut', 'Cotton', 'Wheat', 'Oilseeds']
    },
    'jamnagar': {
        'name': 'APMC Jamnagar',
        'address': 'Bedipara, Jamnagar',
        'contact': '+91-288-2556789',
        'major_crops': ['Groundnut', 'Cotton', 'Wheat', 'Oilseeds']
    },
    'anand': {
        'name': 'APMC Anand',
        'address': 'Anand, Gujarat',
        'contact': '+91-2692-234567',
        'major_crops': ['Maize', 'Wheat', 'Pulses', 'Vegetables']
    },
    'mehsana': {
        'name': 'APMC Mehsana',
        'address': 'Mehsana, Gujarat',
        'contact': '+91-2762-234567',
        'major_crops': ['Cotton', 'Wheat', 'Maize', 'Pulses']
    }
}

# Gujarat Agricultural Universities and Research Centers
GUJARAT_AGRI_INSTITUTIONS = {
    'gsau': {
        'name': 'Gujarat State Agricultural University',
        'location': 'Sardarkrushinagar, Banaskantha',
        'website': 'https://www.gsau.ac.in/',
        'specialization': 'Agricultural research, soil science, crop varieties'
    },
    'icar_nbss': {
        'name': 'ICAR-NBSS&LUP Regional Centre',
        'location': 'Udaipur (serves Gujarat)',
        'website': 'https://nbsslup.in/',
        'specialization': 'Soil survey and land use planning'
    },
    'gujarat_land_use': {
        'name': 'Gujarat State Land Use Board',
        'location': 'Gandhinagar',
        'website': 'https://gslub.gujarat.gov.in/',
        'specialization': 'Land use planning, soil classification'
    }
}

# Gujarat Weather Patterns
GUJARAT_WEATHER_PATTERNS = {
    'summer': {
        'months': ['March', 'April', 'May', 'June'],
        'temperature_range': '30°C - 45°C',
        'humidity': '30% - 60%',
        'rainfall': 'Minimal',
        'crops': 'Cotton, Groundnut, Maize'
    },
    'monsoon': {
        'months': ['July', 'August', 'September'],
        'temperature_range': '25°C - 35°C',
        'humidity': '70% - 90%',
        'rainfall': 'Heavy (500-800mm)',
        'crops': 'Rice, Sugarcane, Vegetables'
    },
    'winter': {
        'months': ['October', 'November', 'December', 'January', 'February'],
        'temperature_range': '15°C - 30°C',
        'humidity': '40% - 70%',
        'rainfall': 'Light to moderate',
        'crops': 'Wheat, Pulses, Oilseeds'
    }
}

# Soil Characteristics by Region
GUJARAT_SOIL_CHARACTERISTICS = {
    'black_soil': {
        'regions': ['north_gujarat', 'central_gujarat'],
        'ph_range': '7.0 - 8.5',
        'nitrogen': 'Medium to high',
        'phosphorus': 'Low to medium',
        'potassium': 'High',
        'organic_carbon': 'Medium',
        'water_retention': 'High',
        'suitable_crops': ['Cotton', 'Wheat', 'Maize', 'Pulses']
    },
    'red_soil': {
        'regions': ['saurashtra'],
        'ph_range': '6.5 - 7.5',
        'nitrogen': 'Low to medium',
        'phosphorus': 'Medium',
        'potassium': 'Medium to high',
        'organic_carbon': 'Low to medium',
        'water_retention': 'Medium',
        'suitable_crops': ['Groundnut', 'Cotton', 'Oilseeds']
    },
    'alluvial_soil': {
        'regions': ['south_gujarat'],
        'ph_range': '6.0 - 7.5',
        'nitrogen': 'Medium to high',
        'phosphorus': 'Medium to high',
        'potassium': 'Medium',
        'organic_carbon': 'High',
        'water_retention': 'High',
        'suitable_crops': ['Rice', 'Sugarcane', 'Vegetables', 'Fruits']
    }
}
