import requests
import os
import json
from dotenv import load_dotenv

def geocodingApi(state_code='', country_code='', limit=1):
    print("Name of the city you're searching:")
    city_name = input()
    print("Pass state code (optional, only for US):")
    state_code = input()
    print("Pass country code (optional):")
    country_code = input()
    load_dotenv()
    API_KEY = os.getenv('OPEN_WEATHER_KEY')
    #Get latitude and longitude
    get_string = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}"
    getCall = requests.get(get_string)
    if getCall.ok:
        responseCall = getCall.json()
        cityName = responseCall[0]['name']
        latitude = responseCall[0]['lat']
        longitude = responseCall[0]['lon']
        #Return forecast
        forecast_string=f"https://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={API_KEY}"
        forecastCall = requests.get(forecast_string)
        responseForecast = forecastCall.json()
        print( "\n", "Nome:", cityName, "\n","Latitude:", latitude, 
              "\n","Longitude:", longitude, "\n", "Current weather:", responseForecast)
    else:
        print("Error: Unable to fetch data from the API")
    

if __name__ == '__main__':
    geocodingApi()