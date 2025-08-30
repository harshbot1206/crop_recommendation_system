from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import pickle
import numpy as np
import json
from .forms import CropForm
from .api_services import api_service

# Load your ML model
try:
    model = pickle.load(open('crop_model.pkl', 'rb'))
except:
    model = None

def home(request):
    """Main view for crop prediction"""
    predicted_crop = None
    crop_info = None
    form = CropForm()
    
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            try:
                # Get form data
                location = form.cleaned_data['location']
                N = form.cleaned_data.get('N', 0)
                P = form.cleaned_data.get('P', 0)
                K = form.cleaned_data.get('K', 0)
                ph = form.cleaned_data.get('ph', 0)
                rainfall = form.cleaned_data.get('rainfall', 0)
                temperature = form.cleaned_data.get('temperature', 0)
                humidity = form.cleaned_data.get('humidity', 0)

                # Predict using model
                if model:
                    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
                    prediction = model.predict(features)
                    predicted_crop = prediction[0]
                    
                    # Get additional information
                    crop_info = get_crop_additional_info(predicted_crop, location)
                else:
                    predicted_crop = "Model not available"

            except Exception as e:
                print("Error during prediction:", e)
                predicted_crop = "Error occurred during prediction"

    return render(request, 'index.html', {
        'form': form,
        'predicted_crop': predicted_crop,
        'crop_info': crop_info
    })

@csrf_exempt
def fetch_location_data(request):
    """API endpoint to fetch data for a location"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            location = data.get('location')
            
            if not location:
                return JsonResponse({'error': 'Location is required'}, status=400)
            
            # Get weather data
            weather_data = api_service.get_weather_data(location)
            if not weather_data:
                return JsonResponse({'error': 'Could not fetch weather data'}, status=400)
            
            # Get coordinates for soil data
            coords = api_service.get_location_coordinates(location)
            soil_data = None
            if coords:
                soil_data = api_service.get_soil_data(coords['lat'], coords['lon'])
            
            # Combine all data
            response_data = {
                'weather': weather_data,
                'soil': soil_data or {},
                'coordinates': coords
            }
            
            return JsonResponse(response_data)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

@csrf_exempt
def get_crop_prices(request):
    """API endpoint to get mandi prices for a crop"""
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            crop_name = data.get('crop')
            
            if not crop_name:
                return JsonResponse({'error': 'Crop name is required'}, status=400)
            
            prices = api_service.get_mandi_prices(crop_name)
            return JsonResponse(prices)
            
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    return JsonResponse({'error': 'Method not allowed'}, status=405)

def get_crop_additional_info(crop_name, location):
    """Get additional information for a crop"""
    try:
        # Get planting and harvest times
        timing_info = api_service.get_planting_harvest_times(crop_name, location)
        
        # Get mandi prices
        price_info = api_service.get_mandi_prices(crop_name)
        
        return {
            'timing': timing_info,
            'prices': price_info
        }
    except Exception as e:
        print(f"Error getting crop info: {e}")
        return None
