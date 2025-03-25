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
    # pprint(weather_data) # This will print in a better way.
    print(f"\nCurrent weather for {weather_data["name"]}\n")
    print(f"\nThe temperature is {weather_data["main"]["temp"]}")
    print(f"\nFeels like {weather_data["main"]["feels_like"]} and {weather_data["weather"][0]["description"]}.")
 
    
if __name__ == "__main__":  
    get_current_weather()