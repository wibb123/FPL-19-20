import json
import numpy as np
from Make_Team_Array import team_name_array, team_strength_array
# import pandas as pd

player_name_array = np.array([],dtype='U20')
player_code_array = np.array([])
gk_2_points_array = np.array([])
gk_3_points_array = np.array([])
gk_4_points_array = np.array([])
gk_5_points_array = np.array([])
df_2_points_array = np.array([])
df_3_points_array = np.array([])
df_4_points_array = np.array([])
df_5_points_array = np.array([])
mf_2_points_array = np.array([])
mf_3_points_array = np.array([])
mf_4_points_array = np.array([])
mf_5_points_array = np.array([])
fw_2_points_array = np.array([])
fw_3_points_array = np.array([])
fw_4_points_array = np.array([])
fw_5_points_array = np.array([])
average_points_array = np.array([])
projected_points_array = np.array([])
player_cost_array = np.array([])
gk_cost_array = np.array([], dtype='i')
df_cost_array = np.array([], dtype='i')
mf_cost_array = np.array([], dtype='i')
fw_cost_array = np.array([], dtype='i')
gk_proj_points_array = np.array([], dtype='float32')
df_proj_points_array = np.array([], dtype='float32')
mf_proj_points_array = np.array([], dtype='float32')
fw_proj_points_array = np.array([], dtype='float32')
gk_name_array = np.array([], dtype='U20')
df_name_array = np.array([], dtype='U20')
mf_name_array = np.array([], dtype='U20')
fw_name_array = np.array([], dtype='U20')
player_position_array = np.array([])

with open("./2019-20/bootstrap","r") as file:
    bootstrap_data = file.read()
    bootstrap_json = json.loads(bootstrap_data)
    all_players = bootstrap_json["elements"]
    all_teams = bootstrap_json["teams"]
    points_array = np.array([[0 for x in range(len(all_teams) * 2)] for x in range(len(all_players))])
    team_h_a_array = np.array([x['name'] + "(H)" for x in all_teams] + [x['name'] + "(A)" for x in all_teams])
    team_strength_array = np.array([x['strength'] for x in all_teams] + [x['strength'] for x in all_teams])
    for j in range(len(all_players)):
        player = all_players[j]
        player_first_name = player['first_name']
        player_second_name = player['second_name']
        player_name = player_first_name + " " + player_second_name
        player_id = player['id']
        player_code = player['code']
        player_position = player['element_type']
        team_id = player['team']
        team = all_teams[team_id - 1]
        team_name = team['name']
        player_path = './2019-20/Teams/' + str(team_name) + '/' + str(player_name)
        with open(player_path,"r") as file:
            player_data = file.read()
            player_json = json.loads(player_data)
            all_fixtures = player_json["history"]
            player_points_array = np.array([])
            play_count = 0
            for i in range(len(all_fixtures)):
                fixture = all_fixtures[i]
                if fixture["minutes"] > 59:
                    play_count = play_count + 1
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
                    if player_position == 1:
                        if team_strength_array[opponent_id - 1] == 2:
                            gk_2_points_array = np.append(gk_2_points_array, points)
                        if team_strength_array[opponent_id - 1] == 3:
                            gk_3_points_array = np.append(gk_3_points_array, points)
                        if team_strength_array[opponent_id - 1] == 4:
                            gk_4_points_array = np.append(gk_4_points_array, points)
                        if team_strength_array[opponent_id - 1] == 5:
                            gk_5_points_array = np.append(gk_5_points_array, points)
                    if player_position == 2:
                        if team_strength_array[opponent_id - 1] == 2:
                            df_2_points_array = np.append(df_2_points_array, points)
                        if team_strength_array[opponent_id - 1] == 3:
                            df_3_points_array = np.append(df_3_points_array, points)
                        if team_strength_array[opponent_id - 1] == 4:
                            df_4_points_array = np.append(df_4_points_array, points)
                        if team_strength_array[opponent_id - 1] == 5:
                            df_5_points_array = np.append(df_5_points_array, points)
                    if player_position == 3:
                        if team_strength_array[opponent_id - 1] == 2:
                            mf_2_points_array = np.append(mf_2_points_array, points)
                        if team_strength_array[opponent_id - 1] == 3:
                            mf_3_points_array = np.append(mf_3_points_array, points)
                        if team_strength_array[opponent_id - 1] == 4:
                            mf_4_points_array = np.append(mf_4_points_array, points)
                        if team_strength_array[opponent_id - 1] == 5:
                            mf_5_points_array = np.append(mf_5_points_array, points)
                    if player_position == 4:
                        if team_strength_array[opponent_id - 1] == 2:
                            fw_2_points_array = np.append(fw_2_points_array, points)
                        if team_strength_array[opponent_id - 1] == 3:
                            fw_3_points_array = np.append(fw_3_points_array, points)
                        if team_strength_array[opponent_id - 1] == 4:
                            fw_4_points_array = np.append(fw_4_points_array, points)
                        if team_strength_array[opponent_id - 1] == 5:
                            fw_5_points_array = np.append(fw_5_points_array, points)
                    player_points_array = np.append(player_points_array,points)
                    points_array[j][pos] = points
                else:
                    continue
            points_array[j][team_id - 1] = 0
            points_array[j][team_id + 19] = 0
        if len(player_points_array) < 5:
            continue
        else:
            average_points = np.average(player_points_array)
            average_points_adjusted = average_points * play_count/len(all_fixtures)
            average_points_array = np.append(average_points_array, average_points_adjusted)
            player_name_array = np.append(player_name_array, player_name)
            player_code_array = np.append(player_code_array, player_code)
            player_position_array = np.append(player_position_array, player_position)

gk_2_average = np.average(gk_2_points_array)
gk_3_average = np.average(gk_3_points_array)
gk_4_average = np.average(gk_4_points_array)
gk_5_average = np.average(gk_5_points_array)
df_2_average = np.average(df_2_points_array)
df_3_average = np.average(df_3_points_array)
df_4_average = np.average(df_4_points_array)
df_5_average = np.average(df_5_points_array)
mf_2_average = np.average(mf_2_points_array)
mf_3_average = np.average(mf_3_points_array)
mf_4_average = np.average(mf_4_points_array)
mf_5_average = np.average(mf_5_points_array)
fw_2_average = np.average(fw_2_points_array)
fw_3_average = np.average(fw_3_points_array)
fw_4_average = np.average(fw_4_points_array)
fw_5_average = np.average(fw_5_points_array)

gk_average = (gk_2_average + gk_3_average + gk_4_average + gk_5_average)/4
df_average = (df_2_average + df_3_average + df_4_average + df_5_average)/4
mf_average = (mf_2_average + mf_3_average + mf_4_average + mf_5_average)/4
fw_average = (fw_2_average + fw_3_average + fw_4_average + fw_5_average)/4
# print("gk 2 average is " + str(gk_2_average))
# print("gk 3 average is " + str(gk_3_average))
# print("gk 4 average is " + str(gk_4_average))
# print("gk 5 average is " + str(gk_5_average))
# print("df 2 average is " + str(df_2_average))
# print("df 3 average is " + str(df_3_average))
# print("df 4 average is " + str(df_4_average))
# print("df 5 average is " + str(df_5_average))
# print("mf 2 average is " + str(mf_2_average))
# print("mf 3 average is " + str(mf_3_average))
# print("mf 4 average is " + str(mf_4_average))
# print("mf 5 average is " + str(mf_5_average))
# print("fw 2 average is " + str(fw_2_average))
# print("fw 3 average is " + str(fw_3_average))
# print("fw 4 average is " + str(fw_4_average))
# print("fw 5 average is " + str(fw_5_average))
# print("gk average is " + str(gk_average))
# print("df average is " + str(df_average))
# print("mf average is " + str(mf_average))
# print("fw average is " + str(fw_average))
# print(points_array)

# for i in range(len(player_name_array)):
#     print(player_name_array[i] + " - " + str(int(player_code_array[i])) + " - " + str(average_points_array[i]))

player_name_array = np.array([],dtype='U20')
with open("./2020-21/bootstrap","r") as file:
    bootstrap_data = file.read()
    bootstrap_json = json.loads(bootstrap_data)
    all_players = bootstrap_json["elements"]
    all_teams = bootstrap_json["teams"]
    for j in range(len(all_players)):
        player = all_players[j]
        player_points = player['total_points']
        player_position = player['element_type']
        player_code = player['code']
        player_first_name = player['first_name']
        player_second_name = player['second_name']
        player_name = player_first_name + " " + player_second_name
        player_cost = player['now_cost']
        player_avail = player['chance_of_playing_next_round']
        code_index_array = np.where(player_code_array == player_code)
        if np.shape(code_index_array) == (1,0):
            continue
        code_index = code_index_array[0]
        if player_position == 3 and player_position_array[code_index] == 2:
            continue
        elif player_avail:
            continue
        else:
            player_average = average_points_array[code_index]
            team_id = player['team']
            team = all_teams[team_id - 1]
            team_name = team['name']
            player_path = './2020-21/Teams/' + str(team_name) + '/' + str(player_name)
            with open(player_path, "r") as file:
                player_data = file.read()
                player_json = json.loads(player_data)
                all_fixtures = player_json["fixtures"]
                first_week = 1
                last_week = 1
                projected_points = np.array([0 for x in range(last_week - first_week + 1)],dtype='f')
                for i in range(len(all_fixtures)):
                    fixture = all_fixtures[i]
                    gameweek = fixture['event']
                    if gameweek > last_week:
                        break
                    fixture_difficulty = fixture['difficulty']
                    if player_position == 1:
                        if fixture_difficulty == 2:
                            projected_points[gameweek - first_week] = (player_average * gk_2_average)/ gk_average
                        if fixture_difficulty == 3:
                            projected_points[gameweek - first_week] = (player_average * gk_3_average)/ gk_average
                        if fixture_difficulty == 4:
                            projected_points[gameweek - first_week] = (player_average * gk_4_average)/ gk_average
                        if fixture_difficulty == 5:
                            projected_points[gameweek - first_week] = (player_average * gk_5_average)/ gk_average
                    if player_position == 2:
                        if fixture_difficulty == 2:
                            projected_points[gameweek - first_week] = (player_average * df_2_average)/ df_average
                        if fixture_difficulty == 3:
                            projected_points[gameweek - first_week] = (player_average * df_3_average)/ df_average
                        if fixture_difficulty == 4:
                            projected_points[gameweek - first_week] = (player_average * df_4_average)/ df_average
                        if fixture_difficulty == 5:
                            projected_points[gameweek - first_week] = (player_average * df_5_average)/ df_average
                    if player_position == 3:
                        if fixture_difficulty == 2:
                            projected_points[gameweek - first_week] = (player_average * mf_2_average)/ mf_average
                        if fixture_difficulty == 3:
                            projected_points[gameweek - first_week] = (player_average * mf_3_average)/ mf_average
                        if fixture_difficulty == 4:
                            projected_points[gameweek - first_week] = (player_average * mf_4_average)/ mf_average
                        if fixture_difficulty == 5:
                            projected_points[gameweek - first_week] = (player_average * mf_5_average)/ mf_average
                    if player_position == 4:
                        if fixture_difficulty == 2:
                            projected_points[gameweek - first_week] = (player_average * fw_2_average)/ fw_average
                        if fixture_difficulty == 3:
                            projected_points[gameweek - first_week] = (player_average * fw_3_average)/ fw_average
                        if fixture_difficulty == 4:
                            projected_points[gameweek - first_week] = (player_average * fw_4_average)/ fw_average
                        if fixture_difficulty == 5:
                            projected_points[gameweek - first_week] = (player_average * fw_5_average)/ fw_average
            total_projected_points = round(sum(projected_points),2)
            print(player_name + " - " + str(total_projected_points))
            projected_points_array = np.append(projected_points_array, total_projected_points)
            player_name_array = np.append(player_name_array, player_name)
            player_cost_array = np.append(player_cost_array, player_cost)
            if player_position == 1:
                gk_proj_points_array = np.append(gk_proj_points_array, total_projected_points)
                gk_cost_array = np.append(gk_cost_array, player_cost)
                gk_name_array = np.append(gk_name_array, player_name)
            if player_position == 2:
                df_proj_points_array = np.append(df_proj_points_array, total_projected_points)
                df_cost_array = np.append(df_cost_array, player_cost)
                df_name_array = np.append(df_name_array, player_name)
            if player_position == 3:
                mf_proj_points_array = np.append(mf_proj_points_array, total_projected_points)
                mf_cost_array = np.append(mf_cost_array, player_cost)
                mf_name_array = np.append(mf_name_array, player_name)
            if player_position == 4:
                fw_proj_points_array = np.append(fw_proj_points_array, total_projected_points)
                fw_cost_array = np.append(fw_cost_array, player_cost)
                fw_name_array = np.append(fw_name_array, player_name)


