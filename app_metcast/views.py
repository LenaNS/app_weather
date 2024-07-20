import requests
from django.shortcuts import render

from .forms import CityForm


def set_coord_city(city: str):
    url = f'https://nominatim.openstreetmap.org/search?q={city}&format=json&accept-language=ru'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return data[0]['lat'], data[0]['lon']
        return None, None
    except Exception as e:
        print('Exception: ' + str(e))
        return None, None    

def get_metcast(latitude: float, longitude: float):
    if not latitude or not longitude:
        return None
    url = f"https://api.open-meteo.com/v1/forecast"
    params = {
        	"latitude": latitude,
	        "longitude": longitude,
	        "hourly": ["temperature_2m", "uv_index"],
            "current": ["temperature_2m"]
    }

    metcast_data = requests.get(url,params).json()
    return metcast_data
    
def metcast_view(request):
    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
            latitude, longitude = set_coord_city(city)
            metcast_data = get_metcast(latitude, longitude)
    else:
            form = CityForm()
            metcast_data = get_metcast(None, None)
            
    context = {
        'metcast_data': metcast_data,
        'form': form
    }
    return render(request, 'app_metcast/main_metcast.html', context)