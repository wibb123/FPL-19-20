import json
import numpy as np

player_number_array = np.array([],dtype='i')
player_id_array = np.array([],dtype='i')
player_name_array = np.array([],dtype='U20')
player_points_array = np.array([],dtype='i')
player_now_cost_array = np.array([],dtype='i')
player_cost_change_start_array = np.array([],dtype='i')
player_start_cost_array = np.array([],dtype='i')
player_position_array = np.array([],dtype='i')

with open("./2019-20/bootstrap","r") as file:
    bootstrap_data = file.read()
    bootstrap_json = json.loads(bootstrap_data)
    all_players = bootstrap_json["elements"]
    all_teams = bootstrap_json["teams"]
    for j in range(len(all_players)):
        player = all_players[j]
        player_points = player['total_points']
        if player_points <= 20:
            continue
        else:
            player_first_name = player['first_name']
            player_second_name = player['second_name']
            player_name = player_first_name + " " + player_second_name
            player_id = player['id']
            player_now_cost = player['now_cost']
            player_cost_change_start = player['cost_change_start']
            player_start_cost = player_now_cost - player_cost_change_start
            player_position = player['element_type']
            player_id_array = np.append(player_id_array,player_id)
            player_name_array = np.append(player_name_array,player_name)
            player_points_array = np.append(player_points_array, player_points)
            player_start_cost_array = np.append(player_start_cost_array, player_start_cost)
            player_position_array = np.append(player_position_array, player_position)

    player_array = np.concatenate([[player_id_array],[player_points_array],[player_start_cost_array],[player_position_array]])
# print(player_array)
