from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm
def index(request):

    appId = 'e5ca5aa02ebc67808dcd1f5581990f91'
    url = 'https://api.openweathermap.org/data/2.5/weather?units=metric&q={}&appid={}'

    if(request.method == 'POST'):
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    cities = City.objects.all()
    all_cities = []

    for city in cities:
        r = requests.get(url.format(city.name, appId)).json()
        city_info = {
            'city': city.name,
            'temp': r['main']['temp'],
            'icon': r['weather'][0]['icon']
        }
        all_cities.append(city_info)

    context = {
        'all_cities': all_cities,
        'form': form
    }
    
    return render(request, 'firstApp/index.html', context)