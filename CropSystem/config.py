import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # OpenWeatherMap API - Free tier available
    OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY', 'af2a48c09a554a0b206f8fa58a30dc97')
    
    # Soil API - User provided key
    SOIL_API_KEY = os.getenv('SOIL_API_KEY', '48mlwO5KAP5ye1vWoAhKLG21CDlHziAV')
    
    # Mandi API - User provided key
    MANDI_API_KEY = os.getenv('MANDI_API_KEY', '9ef84268-d588-465a-a308-a864a43d0070')
    MANDI_API_URL = os.getenv('MANDI_API_URL', 'https://api.mandi.com')
    
    # Database settings
    DATABASE_URL = os.getenv('DATABASE_URL', 'sqlite:///db.sqlite3')
    
    # Logging
    LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO')
    
    # Cache settings
    CACHE_TIMEOUT = int(os.getenv('CACHE_TIMEOUT', 3600))  # 1 hour
