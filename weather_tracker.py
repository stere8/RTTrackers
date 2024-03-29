import requests


class WeatherTracker:
    def __init__(self, region):
        self.region = region
        self.api_token = '83010e9f92f0085b9df45b97e30c635a'  # Replace with your actual token
        self.url = f'http://api.openweathermap.org/data/2.5/weather?q={region}&appid={self.api_token}&units=metric'

    def get_current_weather_data(self):
        res = requests.get(self.url)
        data = res.json()  # Parse JSON response

        if 'main' in data:
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            temp = data['main']['temp']
        else:
            humidity = None
            pressure = None
            temp = None

        if 'wind' in data:
            wind_speed = data['wind']['speed']
        else:
            wind_speed = None

        if 'weather' in data and len(data['weather']) > 0:
            description = data['weather'][0]['description']
        else:
            description = None

        return humidity, pressure, wind_speed, description, temp
