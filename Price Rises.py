import json
import numpy as np



with open("./2019-20/bootstrap","r") as file:
    bootstrap_data = file.read()
    bootstrap_json = json.loads(bootstrap_data)
    all_players = bootstrap_json["elements"]
    all_teams = bootstrap_json["teams"]
    rise_array = np.array([[0 for x in range(6)] for x in range(48)])
    print(rise_array)
    # team_h_a_array = np.array([x['name'] + "(H)" for x in all_teams] + [x['name'] + "(A)" for x in all_teams])
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
        # player_name_array = np.append(player_name_array, player_name)
        with open(player_path,"r") as file:
            player_data = file.read()
            player_json = json.loads(player_data)
            all_fixtures = player_json["history"]
            for i in range(len(all_fixtures) - 1):
                fixture = all_fixtures[i]
                next_fixture = all_fixtures[i+1]
                value = fixture["value"]
                next_value = next_fixture["value"]
                gameweek = next_fixture["round"]
                if value == next_value:
                    continue
                elif value == next_value + 1:
                    rise = next_value - value
                    # print(player_name + " " + str(rise/10) + " " + str(gameweek))
                    rise_array[gameweek,0] = rise_array[gameweek,0] + 1
                elif value == next_value + 2:
                    rise = next_value - value
                    print(player_name + " " + str(rise/10) + " " + str(gameweek))
                    rise_array[gameweek, 1] = rise_array[gameweek, 1] + 1
                elif value == next_value + 3:
                    rise = next_value - value
                    # print(player_name + " " + str(rise/10) + " " + str(gameweek))
                    rise_array[gameweek, 2] = rise_array[gameweek, 2] + 1
                elif value == next_value - 1:
                    rise = next_value - value
                    # print(player_name + " " + str(rise/10) + " " + str(gameweek))
                    rise_array[gameweek,3] = rise_array[gameweek,3] + 1
                elif value == next_value - 2:
                    rise = next_value - value
                    print(player_name + " " + str(rise/10) + " " + str(gameweek))
                    rise_array[gameweek,4] = rise_array[gameweek,4] + 1
                else:
                    fall = value - next_value
                    # print(player_name + " " + str(fall/10) + " " + str(gameweek))
                    rise_array[gameweek,5] = rise_array[gameweek,5] + 1


print(rise_array)
