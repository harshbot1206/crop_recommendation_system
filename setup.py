#!/usr/bin/env python3
"""
Setup script for Crop Recommendation System
"""

import os
import subprocess
import sys

def install_requirements():
    """Install required packages"""
    print("📦 Installing required packages...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Packages installed successfully!")
    except subprocess.CalledProcessError:
        print("❌ Failed to install packages. Please install manually:")
        print("   pip install -r requirements.txt")
        return False
    return True

def create_env_file():
    """Create .env file if it doesn't exist"""
    env_file = ".env"
    if os.path.exists(env_file):
        print("✅ .env file already exists")
        return True
    
    print("🔑 Creating .env file...")
    env_content = """# Crop Recommendation System - Environment Variables
# Fill in your actual API keys

# OpenWeatherMap API (Free tier: 1000 calls/day)
# Sign up at: https://openweathermap.org/api
OPENWEATHER_API_KEY=your_openweather_api_key_here

# SoilGrids API (Free tier available)
# Sign up at: https://www.isric.org/explore/soilgrids/soilgrids-rest-api
SOILGRIDS_API_KEY=your_soilgrids_api_key_here

# Mandi API (You'll need to find a suitable API)
MANDI_API_KEY=your_mandi_api_key_here
MANDI_API_URL=https://api.mandi.com

# Database settings
DATABASE_URL=sqlite:///db.sqlite3

# Logging level
LOG_LEVEL=INFO

# Cache timeout in seconds
CACHE_TIMEOUT=3600
"""
    
    try:
        with open(env_file, 'w') as f:
            f.write(env_content)
        print("✅ .env file created successfully!")
        print("⚠️  Please edit .env file and add your actual API keys")
        return True
    except Exception as e:
        print(f"❌ Failed to create .env file: {e}")
        return False

def run_migrations():
    """Run Django migrations"""
    print("🗄️  Running database migrations...")
    try:
        subprocess.check_call([sys.executable, "manage.py", "migrate"])
        print("✅ Migrations completed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to run migrations")
        return False

def main():
    """Main setup function"""
    print("🌱 Welcome to Crop Recommendation System Setup!")
    print("=" * 50)
    
    # Check if we're in the right directory
    if not os.path.exists("manage.py"):
        print("❌ Please run this script from the project root directory")
        return
    
    # Install requirements
    if not install_requirements():
        return
    
    # Create .env file
    if not create_env_file():
        return
    
    # Run migrations
    if not run_migrations():
        return
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Edit .env file and add your API keys")
    print("2. Run: python manage.py runserver")
    print("3. Visit: http://localhost:8000")
    print("\n📚 For detailed setup instructions, see README.md")
    print("\n🔑 API Key Generation:")
    print("- OpenWeatherMap: https://openweathermap.org/api")
    print("- SoilGrids: https://www.isric.org/explore/soilgrids/soilgrids-rest-api")
    print("- Mandi APIs: See README.md for options")

if __name__ == "__main__":
    main()
