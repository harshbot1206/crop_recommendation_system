from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/fetch-location-data/', views.fetch_location_data, name='fetch_location_data'),
    path('api/get-crop-prices/', views.get_crop_prices, name='get_crop_prices'),
]
