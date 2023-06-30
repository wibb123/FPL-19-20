import json
import numpy as np

team_id_array = np.array([],dtype='i')
team_name_array = np.array([],dtype='U20')
team_strength_array = np.array([],dtype='i')


with open("./2019-20/bootstrap","r") as file:
    bootstrap_data = file.read()
    bootstrap_json = json.loads(bootstrap_data)
    all_players = bootstrap_json["elements"]
    all_teams = bootstrap_json["teams"]
    for team in all_teams:
        team_name = team["name"]
        team_id = team["id"]
        team_strength = team["strength"]
        position = np.searchsorted(team_id_array,team_id)
        team_id_array = np.append(team_id_array,team_id)
        team_name_array = np.append(team_name_array,team_name)
        team_strength_array = np.append(team_strength_array,team_strength)

    team_array = np.concatenate([[team_id_array],[team_name_array]])