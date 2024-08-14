
from django.shortcuts import render
from django.contrib import messages
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'kanpur'
    
    # Weather API
    weather_url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=d81e278eb19122b81b90f62a5f5cfad8'
    PARAMS = {'units': 'metric'}

    # Google Custom Search API
    API_KEY = 'AIzaSyA5xayWZ1RIcT2zxoNxTDHZ4KyVlVt6HW4'
    SEARCH_ENGINE_ID = 'a5d263850e1304083'
    query = city + " 1920x1080"
    page = 1
    start = (page - 1) * 10 + 1
    searchType = 'image'
    city_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}&searchType={searchType}&imgSize=xlarge"

    try:
        # Fetch background image
        data = requests.get(city_url).json()
        search_items = data.get("items")

        if search_items:
            image_url = search_items[0]['link']  # Fetch the first image result
        else:
            image_url = 'https://images.pexels.com/photos/3008509/pexels-photo-3008509.jpeg?auto=compress&cs=tinysrgb&w=1600'  # Replace with a valid default image URL

        # Fetch weather data
        weather_data = requests.get(weather_url, params=PARAMS).json()
        description = weather_data['weather'][0]['description']
        icon = weather_data['weather'][0]['icon']
        temp = weather_data['main']['temp']
        day = datetime.date.today()

        return render(request, 'weatherapp/index.html', {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city,
            'exception_occurred': False,
            'image_url': image_url
        })

    except KeyError:
        exception_occurred = True
        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': datetime.date.today(),
            'city': 'kanpur',
            'exception_occurred': exception_occurred
        })
    except requests.RequestException as e:
        # Handle network-related errors
        print(f"Network error: {e}")
        exception_occurred = True
        return render(request, 'weatherapp/index.html', {
            'description': 'clear sky',
            'icon': '01d',
            'temp': 25,
            'day': datetime.date.today(),
            'city': 'kanpur',
            'exception_occurred': exception_occurred
        })
