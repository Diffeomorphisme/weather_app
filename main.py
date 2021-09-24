import json
from urllib.request import urlopen
from urllib.parse import urlencode


class WeatherData:
    def __init__(self, location: str):
        self.location = location

    def current_temperature_c(self):
        json_object = self.current_data()
        return json_object["current"]["temp_c"]

    def current_data(self):
        url = "http://api.weatherapi.com/v1/current.json"
        parameters = {"key": "d40a289346714e398d0141905212309", "q": self.location}
        data = urlencode(parameters, encoding='utf-8')
        data_b = data.encode()
        response = urlopen(url, data_b)
        json_object = json.load(response)
        return json_object


city = "Göteborg"
weather = WeatherData(city)
print("The temperature in", city, "is currently", str(weather.current_temperature_c()))
