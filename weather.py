from settings import weather_token as wt
import requests
import datetime
from dWeather import DataWeather


def get_weather(city, weather_token=wt):
    r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_token}&units=metric')
    data = r.json()
    weather_data = DataWeather()
    weather_data.set_city(data['name'])
    weather_data.set_temp(data['main']['temp'])
    weather_data.set_humidity(data['main']['humidity'])
    weather_data.set_pressure(data['main']['pressure'])
    weather_data.set_wind(data['wind']['speed'])
    weather_data.set_sunrise(datetime.datetime.fromtimestamp(data['sys']['sunrise']))
    weather_data.set_sunset(datetime.datetime.fromtimestamp(data['sys']['sunset']))
    return weather_data
