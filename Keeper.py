import numpy as np
import json

keeper_points = []

for i in range(1,48):
    with open(".\\2019-20\HarryWillyBoly\MyPicks\Gameweek" + str(i),"r") as file:
        gameweek_data = file.read()
        gameweek_json = json.loads(gameweek_data)
        players = gameweek_json["picks"]
        keeper = players[0]
        keeper_id = keeper["element"]
    with open(".\\2019-20\HarryWillyBoly\Points\Gameweek" + str(i),"r") as file:
        gameweek_data = file.read()
        gameweek_json = json.loads(gameweek_data)
        players = gameweek_json["elements"]
        for player in players:
            if player["id"] == keeper_id:
                player_stats = player["stats"]
                keeper_points.append(player_stats["total_points"])

print(sum(keeper_points))
print(keeper_points)
