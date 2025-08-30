# 🌱 Smart Crop Recommendation System

An intelligent crop recommendation system that automatically fetches soil and weather data based on location, predicts optimal crops, and provides planting/harvest timing and market prices.

## ✨ Features

- **Auto-Fetch Data**: Automatically retrieves N, P, K, pH, rainfall, temperature, and humidity based on location
- **Smart Crop Prediction**: Uses machine learning to recommend the best crop for your conditions
- **Optimal Timing**: Provides best planting and harvest times for recommended crops
- **Market Prices**: Shows current mandi prices for crops
- **Beautiful UI**: Modern, responsive interface with real-time data updates
- **Location-Based**: Works with any city in India

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone <your-repo-url>
cd crop_recommendation_system
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Set Up API Keys
Create a `.env` file in the root directory with your API keys:

```env
# OpenWeatherMap API (Free tier: 1000 calls/day)
OPENWEATHER_API_KEY=your_openweather_api_key_here

# SoilGrids API (Free tier available)
SOILGRIDS_API_KEY=your_soilgrids_api_key_here

# Mandi API
MANDI_API_KEY=your_mandi_api_key_here
MANDI_API_URL=https://api.mandi.com
```

### 4. Run the Application
```bash
python manage.py runserver
```

Visit `http://localhost:8000` in your browser.

## 🔑 API Key Generation Steps

### 1. OpenWeatherMap API (Weather Data)
1. Go to [OpenWeatherMap](https://openweathermap.org/api)
2. Click "Sign Up" and create a free account
3. Go to "My API Keys" section
4. Copy your API key
5. **Free tier**: 1000 calls/day, 60 calls/minute

### 2. SoilGrids API (Soil Data)
1. Visit [SoilGrids](https://www.isric.org/explore/soilgrids/soilgrids-rest-api)
2. Click "Get API Key"
3. Fill out the registration form
4. Check your email for the API key
5. **Free tier**: Available with registration

### 3. Mandi Price API (Market Data)
You have several options for mandi prices:

#### Option A: Government of India APIs
- [eNAM API](https://enam.gov.in/web/) - National Agriculture Market
- [Agmarknet](http://agmarknet.gov.in/) - Agricultural Marketing Information Network

#### Option B: Private APIs
- [Krishi Jagran](https://krishijagran.com/)
- [AgriFarming](https://www.agrifarming.in/)

#### Option C: Create Your Own Database
- Collect data from government websites
- Use web scraping (with permission)
- Partner with local mandis

## 🏗️ System Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │   Django        │    │   External      │
│   (HTML/JS)     │◄──►│   Backend       │◄──►│   APIs          │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                              │
                              ▼
                       ┌─────────────────┐
                       │   ML Model      │
                       │   (crop_model.pkl)│
                       └─────────────────┘
```

## 📁 Project Structure

```
crop_recommendation_system/
├── CropSystem/
│   ├── api_services.py      # External API integrations
│   ├── forms.py             # Django forms
│   ├── views.py             # Business logic
│   ├── urls.py              # URL routing
│   ├── templates/
│   │   └── index.html       # Main interface
│   └── static/
│       ├── css/
│       └── js/
├── requirements.txt          # Python dependencies
├── config.py                # Configuration settings
├── manage.py                # Django management
└── README.md               # This file
```

## 🔧 Configuration

### Environment Variables
- `OPENWEATHER_API_KEY`: Your OpenWeatherMap API key
- `SOILGRIDS_API_KEY`: Your SoilGrids API key
- `MANDI_API_KEY`: Your Mandi API key
- `MANDI_API_URL`: Base URL for mandi API
- `LOG_LEVEL`: Logging level (INFO, DEBUG, ERROR)
- `CACHE_TIMEOUT`: Cache timeout in seconds

### Customization
- Modify `api_services.py` to add new APIs
- Update `crop_calendar` in `get_planting_harvest_times()` for more crops
- Customize the ML model in `train_model.py`

## 🌾 Supported Crops

The system currently supports:
- Rice
- Wheat
- Maize
- Cotton
- Sugarcane
- And more (based on your ML model)

## 📊 Data Sources

- **Weather**: OpenWeatherMap API
- **Soil**: SoilGrids API (ISRIC)
- **Market Prices**: Various mandi APIs
- **Crop Calendar**: Built-in database (expandable)

## 🚨 Troubleshooting

### Common Issues

1. **API Key Errors**
   - Verify your API keys are correct
   - Check API rate limits
   - Ensure keys are properly set in `.env`

2. **Location Not Found**
   - Use standard city names
   - Check spelling
   - Try nearby major cities

3. **Model Loading Error**
   - Ensure `crop_model.pkl` exists
   - Check file permissions
   - Verify model compatibility

### Debug Mode
Set `LOG_LEVEL=DEBUG` in your `.env` file for detailed logging.

## 🔒 Security Notes

- Never commit your `.env` file
- Use environment variables for sensitive data
- Implement rate limiting for production
- Add authentication for production use

## 🚀 Production Deployment

1. Set `DEBUG=False` in `settings.py`
2. Configure a production database
3. Set up proper logging
4. Use a production web server (Gunicorn, uWSGI)
5. Configure HTTPS
6. Set up monitoring and alerts

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- OpenWeatherMap for weather data
- SoilGrids for soil information
- Government of India for agricultural data
- Django community for the web framework

## 📞 Support

For support and questions:
- Create an issue on GitHub
- Check the troubleshooting section
- Review API documentation

---

**Happy Farming! 🌾🌱**
