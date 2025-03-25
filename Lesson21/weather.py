import requests
from dotenv import load_dotenv
import os
from pprint import pprint

load_dotenv()

def get_current_weather():
    print("\n*** Get Current Weather Conditions ***\n")
    city = input("\nPlease enter a city name:\n")

    request_url = f'https://api.openweathermap.org/data/2.5/weather?appid={os.getenv("API_KEY")}&q={city}&units=metric'
    
    #print(request_url)
    
    weather_data = requests.get(request_url).json() # making a get request
    #print(weather_data) # prints the json. 
    pprint(weather_data) # This will print in a better way.
 
    

get_current_weather()