import requests
import pprint
from datetime import datetime

weathers = []

class Weather:
    def __init__(self, name, temp_c):
    
        self.name =  name
        self.temp_c = temp_c
        self.localtime = datetime.today().date()

    def read(self):
        with open("pogoda.txt", "r") as file:
            for line in file.readlines():
                self.name = line.split(',')[0]
                self.localtime = line.split(',')[1]
                self.temp_c = line.split(',')[2].split("\n")[0]

    def __str__(self):
        return f"{self.name}, {self.temp_c}, {self.localtime}"
    
    def save(self):
        with open("pogoda.txt", "a") as file:
            file.write(str(self.name) + ',' + str(self.localtime) + ',' + str(self.temp_c) + '\n')
    
miasto = input("Miasto: ")
 
date = str(input('date (YYYY, MM, D) :'))
try:
    dt_start = datetime.strptime(date, '%Y, %m, %d')
except ValueError:
    print ("Incorrect format")

class GetDate:
    
    def __init__(self, url):
        self.url = url 
        self.data = self.get_data()

    def get_data(self):
        r = requests.get(self.url)
        return r.json()

data = GetDate(f"http://api.weatherapi.com/v1/current.json?key=41c0cc296c424df4a7f182052212406&q= + {miasto} + '&days=' + {date} +  &aqi=no")

print(data.data["current"]["temp_c"])

weather = Weather(miasto, data.data["current"]["temp_c"])
weathers.append(weather)


weather.save()