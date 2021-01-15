import os
import requests
import json
import sys
from datetime import date

def data_prognozy():
    # Czy jest data w argv?
    #if not sys.argv[1]:
    if len(sys.argv) < 3:   # todo doczytaj czemu len, a nie if
        data_do_sprawdzenia = str(date.today())
    else:
        data_do_sprawdzenia = sys.argv[2]
    return data_do_sprawdzenia


def odczyt_API():
    if os.path.exists("pogoda.txt"):
        with open("pogoda.txt", "r") as f:
            lst = json.loads(f.read())
            print("wczytane z pogoda.txt")
    else:
        url = "https://dark-sky.p.rapidapi.com/52.25,21"
        querystring = {"lang": "en", "units": "auto"}
        headers = {
            'x-rapidapi-key': sys.argv[1],
            'x-rapidapi-host': "dark-sky.p.rapidapi.com"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        lst = response.json()
        fp = open("pogoda.txt", "w")
        fp.write(response.text)
        fp.close()
    return lst
#    print(lst)
    # print(response.text) - oryginalnie z Rapidapi

weather_data = odczyt_API()
#print(weather_data["daily"]["data"][0]["time"])
#print(weather_data["daily"]["data"][0]["icon"])
#print(str(date.fromtimestamp(weather_data["daily"]["data"][0]["time"])))

znaleziono_prognoze = False

for dane in weather_data["daily"]["data"]:
    data_spr = str(date.fromtimestamp(dane["time"]))
    if data_spr != data_prognozy():
        continue # todo sprawdź czemu to działa
    znaleziono_prognoze = True
    if dane["icon"] == "rain" or dane["icon"] == "snow":
        print("Będzie padać, Robert")
    else:
        print("Robert, nie będzie padać")
if not znaleziono_prognoze:
    print("Nie wiem, Robert... Nie wiem.")
