import requests
import pprint
from requests.auth import HTTPBasicAuth
import datetime

weathers = []

class Weather:
    def __init__(self, name, temp_c, localtime):
    
        self.name = name
        self.temp_c = temp_c
        self.localtime = localtime

    def __int__(self):
        return f"{self.name}, {self.temp_c}, {self.localtime}"
    
    def save(self):
        with open("pogoda.txt", "a") as file:
            file.write(str())
    
#    def read_saldo(self):
#        with open("pogoda.txt", "r") as file:
#            for line in file.readlines():


class GetDate:
    
    def __init__(self, url):
        self.url = url 
        self.data = self.get_data()

    def get_data(self):
        r = requests.get('http://api.weatherapi.com/v1/current.json?key=41c0cc296c424df4a7f182052212406&q=Poland&aqi=no')
        return r.json()

data = GetDate("http://api.weatherapi.com/v1/current.json?key=41c0cc296c424df4a7f182052212406&q=Poland&aqi=no")

for entry in data.data:
    weather = Weather(entry["location"]["name"], entry["location"]["localtime"], entry["condition"]["temp_c"])
    weathers.append(weather)

print(weathers[-1].name)