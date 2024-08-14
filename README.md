Weather App
A simple weather application built with Django that provides current weather information and dynamic city backgrounds.

Features
Current Weather Data: Fetches real-time weather information using the OpenWeatherMap API.
Dynamic City Backgrounds: Uses the Google Custom Search API to fetch city images and set them as backgrounds.


Technologies Used
Django: Web framework for building the application.
OpenWeatherMap API: Provides weather data.
Google Custom Search API: Retrieves city images for backgrounds.

Setup
Prerequisites
Python 3.8+
Django 4.0+
Requests library

Installation
Clone the repository:
git clone https://github.com/arpitshakya23/weather-app.git


Navigate to the project directory:
cd weather-app


Install the required packages:
pip install -r requirements.txt


Set up your environment variables for API keys:
Create a .env file in the root directory with the following content:
OPENWEATHERMAP_API_KEY=your_openweathermap_api_key
GOOGLE_CUSTOM_SEARCH_API_KEY=your_google_custom_search_api_key
GOOGLE_CUSTOM_SEARCH_ENGINE_ID=your_google_custom_search_engine_id


Run database migrations:
python manage.py migrate


Start the development server:
python manage.py runserver
Visit http://127.0.0.1:8000/ in your web browser to view the app.

Configuration
Update settings.py with your API keys if you prefer not to use environment variables.

Usage
Enter a city name in the search bar.
View the current weather data and city background image.


Contributing
Feel free to open issues or submit pull requests. Contributions are welcome!


Contact
Arpit Shakya
shakyaarpit1028@gmail.com
