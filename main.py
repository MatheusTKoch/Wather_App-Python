import requests
import os

def geocodingApi(state_code='', country_code='', limit=1):
    print("Name of the city you're searching:")
    city_name = input()
    print("Pass state code (optional, only for US):")
    state_code = input()
    print("Pass country code (optional):")
    country_code = input()
    API_KEY = '2e76442c50caf73a70575f6d13b21521' #os.environ['OPEN_WEATHER_KEY']
    get_string = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_KEY}"
    getCall = requests.get(get_string)
    reponseCall = getCall.content
    responseSplit = str(reponseCall).split('b')
    print( "Nome:", responseSplit[1]["name"])

if __name__ == '__main__':
    geocodingApi()