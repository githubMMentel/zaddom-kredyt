import os
import requests
import json
import sys
from datetime import date

class WeatherForecast:

    def __init__(self):
        self.weather_data = self.odczyt_API()

    def data_prognozy(self):
        # Czy jest data w argv?
        if len(sys.argv) < 3:
            data_do_sprawdzenia = str(date.today())
        else:
            data_do_sprawdzenia = sys.argv[2]
        return data_do_sprawdzenia

    def odczyt_API(self, force=False):
        if os.path.exists("weather/pogoda.txt") and not force:
            with open("weather/pogoda.txt", "r") as f:
                lst = json.loads(f.read())
                print("wczytane z pogoda.txt")
        else:
            url = "https://dark-sky.p.rapidapi.com/52.25,21"
            querystring = {"lang": "en", "units": "auto"}
            headers = {
                'x-rapidapi-key': sys.argv[1],
                'x-rapidapi-host': "dark-sky.p.rapidapi.com"
            }
            response = requests.request(
                "GET", url, headers=headers, params=querystring
            )
            lst = response.json()
            fp = open("weather/pogoda.txt", "w")
            fp.write(response.text)
            fp.close()
        return lst

    def items(self):
        for dane in self.weather_data["daily"]["data"]:
            data_spr = str(date.fromtimestamp(dane["time"]))
            if dane["icon"] == "rain" or dane["icon"] == "snow":
                yield (data_spr, "Będzie padać Robert.")
            else:
                yield (data_spr, "Robert, nie będzie padać.")

    def getitem_local(self, data_prognozy):
        znaleziono_prognoze = False
        for dane in self.weather_data["daily"]["data"]:
            data_spr = str(date.fromtimestamp(dane["time"]))
            if data_spr != data_prognozy:
                continue # todo sprawdź czemu to działa
            znaleziono_prognoze = True
            if dane["icon"] == "rain" or dane["icon"] == "snow":
                return "Będzie padać, Robert"
            else:
                return "Robert, nie będzie padać"
        if not znaleziono_prognoze:
            return "Nie wiem Robert, nie wiem sam..."

    def __getitem__(self, data_prognozy):
        retval = self.getitem_local(data_prognozy)
        if retval != "Nie wiem Robert... Nie wiem.":
            return retval
        self.weather_data = self.odczyt_API(force=True) # lub odczyt_API(True)
        return self.getitem_local(data_prognozy)

wf = WeatherForecast()

print(wf.data_prognozy())
print(wf[wf.data_prognozy()])

# for data, prognoza in wf.items():
#     print("{} {}".format(data, prognoza))
