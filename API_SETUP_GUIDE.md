# 🚀 **API Setup Guide for Gujarat Crop Recommendation System**

## 🔑 **Your API Keys (Already Configured):**
- **Soil API Key**: `48mlwO5KAP5ye1vWoAhKLG21CDlHziAV`
- **Mandi Price API Key**: `9ef84268-d588-465a-a308-a864a43d0070`

## 📍 **To Complete Setup, You Need to Provide:**

### **1. Soil API Endpoint**
**File to edit**: `CropSystem/api_endpoints.py`

**Find this line:**
```python
'base_url': 'https://api.soilservice.com',  # Replace with your actual soil API URL
```

**Replace with your actual soil API URL**, for example:
```python
'base_url': 'https://your-soil-api.com',
```

### **2. Mandi Price API Endpoint**
**File to edit**: `CropSystem/api_endpoints.py`

**Find this line:**
```python
'base_url': 'https://api.mandiprices.com',  # Replace with your actual mandi API URL
```

**Replace with your actual mandi API URL**, for example:
```python
'base_url': 'https://your-mandi-api.com',
```

## 🔍 **How to Find Your API Endpoints:**

1. **Check your API documentation** - it should list the base URL
2. **Look at your API key email** - it usually includes the endpoint
3. **Check your developer dashboard** - if you have one
4. **Look for any API documentation** you received

## 📝 **Example of What You Need:**

```
Soil API Base URL: https://api.soilservice.com
Mandi API Base URL: https://api.mandiprices.com
```

## ✅ **What Happens After Setup:**

- **Real-time soil data** (N, P, K, pH) for Gujarat locations
- **Live mandi prices** from Gujarat markets
- **Accurate crop recommendations** based on real conditions
- **No more dummy data** - everything will be real-time

## 🚨 **Important Notes:**

- **Never share your API keys** publicly
- **Keep your .env file secure** and don't commit it to version control
- **Test with small queries first** to ensure everything works
- **Check API rate limits** to avoid hitting limits

## 🆘 **Need Help?**

If you can't find your API endpoints, please:
1. Check your email for API documentation
2. Look for any developer portal or dashboard
3. Contact the API provider's support
4. Share any documentation you have

## 🎯 **Quick Test:**

After setting the endpoints:
1. Restart your Django server
2. Visit `http://localhost:8000`
3. Enter a Gujarat city (e.g., Ahmedabad)
4. Click "Auto-Fill"
5. Check if real data is fetched

**Your system is ready to use real APIs - just provide the endpoints!** 🚀
