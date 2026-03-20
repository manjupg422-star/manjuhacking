import requests
import json

class WeatherDashboard:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"

    def get_current_weather(self, city):
        endpoint = f"{self.base_url}weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(endpoint)
        return response.json()

    def get_5_day_forecast(self, city):
        endpoint = f"{self.base_url}forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(endpoint)
        return response.json()

    def get_weather_by_coordinates(self, lat, lon):
        endpoint = f"{self.base_url}weather?lat={lat}&lon={lon}&appid={self.api_key}&units=metric"
        response = requests.get(endpoint)
        return response.json()

    def get_air_quality(self, lat, lon):
        air_quality_base_url = "http://api.openweathermap.org/data/2.5/air_pollution"
        endpoint = f"{air_quality_base_url}?lat={lat}&lon={lon}&appid={self.api_key}"
        response = requests.get(endpoint)
        return response.json()

# Example usage
if __name__ == '__main__':
    API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
    dashboard = WeatherDashboard(API_KEY)
    print(dashboard.get_current_weather('London'))
    print(dashboard.get_5_day_forecast('London'))
    print(dashboard.get_weather_by_coordinates(51.5074, -0.1278))
    print(dashboard.get_air_quality(51.5074, -0.1278))
