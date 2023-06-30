import json
import numpy as np
from Make_Team_Array import team_name_array, team_strength_array
# import pandas as pd

player_name_array = np.array([],dtype='U20')

with open("./2019-20/bootstrap","r") as file:
    bootstrap_data = file.read()
    bootstrap_json = json.loads(bootstrap_data)
    all_players = bootstrap_json["elements"]
    all_teams = bootstrap_json["teams"]
    points_array = np.array([[0 for x in range(len(all_teams) * 2)] for x in range(len(all_players))])
    team_h_a_array = np.array([x['name'] + "(H)" for x in all_teams] + [x['name'] + "(A)" for x in all_teams])
    for j in range(len(all_players)):
        player = all_players[j]
        player_first_name = player['first_name']
        player_second_name = player['second_name']
        player_name = player_first_name + " " + player_second_name
        player_id = player['id']
        team_id = player['team']
        team = all_teams[team_id - 1]
        team_name = team['name']
        player_path = './2019-20/Teams/' + str(team_name) + '/' + str(player_name)
        player_name_array = np.append(player_name_array, player_name)
        with open(player_path,"r") as file:
            player_data = file.read()
            player_json = json.loads(player_data)
            all_fixtures = player_json["history"]
            for i in range(len(all_fixtures)):
                fixture = all_fixtures[i]
                opponent_id = fixture["opponent_team"]
                opponent = team_name_array[opponent_id-1]
                points = fixture["total_points"]
                is_home = fixture["was_home"]
                if is_home == True:
                    h_a = '(H)'
                    h_a_ind = 0
                else:
                    h_a = '(A)'
                    h_a_ind = 20
                pos = opponent_id - 1 + h_a_ind
                opponent_h_a = opponent + h_a
                points_array[j][pos] = points
            points_array[j][team_id - 1] = 0
            points_array[j][team_id + 19] = 0

# data = pd.DataFrame(points_array, index=[player_name_array], columns=[team_h_a_array])
# print(data)

# data.to_csv("output_filename.csv", index=True, encoding='utf8')
