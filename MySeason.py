from urllib.request import urlopen
import json
import os


for j in range(1,48):
    url = "https://fantasy.premierleague.com/api/event/" + str(j) + "/live/"
    file_name = "Gameweek" + str(j)
    path = '.\Extracts\HarryWillyBoly\Points\\' + str(file_name)
    url_open = urlopen(url)
    data = url_open.read()
    data_json = json.loads(data)
    with open(path, "w") as file:
        json.dump(data_json, file, indent=2)
