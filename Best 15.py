import numpy as np
import json
from knapsack import knapSackE, knapSack, knapSackEE

gk_name_array = np.array([], dtype='U20')
gk_id_array = np.array([], dtype='i')
gk_points_array = np.array([], dtype='i')
gk_start_cost_array = np.array([], dtype='i')
df_name_array = np.array([], dtype='U20')
df_id_array = np.array([], dtype='i')
df_points_array = np.array([], dtype='i')
df_start_cost_array = np.array([], dtype='i')
mf_name_array = np.array([], dtype='U20')
mf_id_array = np.array([], dtype='i')
mf_points_array = np.array([], dtype='i')
mf_start_cost_array = np.array([], dtype='i')
fw_name_array = np.array([], dtype='U20')
fw_id_array = np.array([], dtype='i')
fw_points_array = np.array([], dtype='i')
fw_start_cost_array = np.array([], dtype='i')


with open("./2020-21/bootstrap","r") as file:
    bootstrap_data = file.read()
    bootstrap_json = json.loads(bootstrap_data)
    all_players = bootstrap_json["elements"]
    all_teams = bootstrap_json["teams"]
    for j in range(len(all_players)):
        player = all_players[j]
        player_points = player['total_points']
        player_position = player['element_type']
        if player_points <= 20:
            continue
        else:
            if player_position == 1:
                gk_first_name = player['first_name']
                gk_second_name = player['second_name']
                gk_name = gk_first_name + " " + gk_second_name
                gk_id = player['id']
                gk_now_cost = player['now_cost']
                gk_cost_change_start = player['cost_change_start']
                gk_start_cost = gk_now_cost - gk_cost_change_start
                gk_id_array = np.append(gk_id_array,gk_id)
                gk_name_array = np.append(gk_name_array,gk_name)
                gk_points_array = np.append(gk_points_array, player_points)
                gk_start_cost_array = np.append(gk_start_cost_array, gk_start_cost)
            elif player_position == 2:
                df_first_name = player['first_name']
                df_second_name = player['second_name']
                df_name = df_first_name + " " + df_second_name
                df_id = player['id']
                df_now_cost = player['now_cost']
                df_cost_change_start = player['cost_change_start']
                df_start_cost = df_now_cost - df_cost_change_start
                df_id_array = np.append(df_id_array,df_id)
                df_name_array = np.append(df_name_array,df_name)
                df_points_array = np.append(df_points_array, player_points)
                df_start_cost_array = np.append(df_start_cost_array, df_start_cost)
            elif player_position == 3:
                mf_first_name = player['first_name']
                mf_second_name = player['second_name']
                mf_name = mf_first_name + " " + mf_second_name
                mf_id = player['id']
                mf_now_cost = player['now_cost']
                mf_cost_change_start = player['cost_change_start']
                mf_start_cost = mf_now_cost - mf_cost_change_start
                mf_id_array = np.append(mf_id_array,mf_id)
                mf_name_array = np.append(mf_name_array,mf_name)
                mf_points_array = np.append(mf_points_array, player_points)
                mf_start_cost_array = np.append(mf_start_cost_array, mf_start_cost)
            elif player_position == 4:
                fw_first_name = player['first_name']
                fw_second_name = player['second_name']
                fw_name = fw_first_name + " " + fw_second_name
                fw_id = player['id']
                fw_now_cost = player['now_cost']
                fw_cost_change_start = player['cost_change_start']
                fw_start_cost = fw_now_cost - fw_cost_change_start
                fw_id_array = np.append(fw_id_array,fw_id)
                fw_name_array = np.append(fw_name_array,fw_name)
                fw_points_array = np.append(fw_points_array, player_points)
                fw_start_cost_array = np.append(fw_start_cost_array, fw_start_cost)


included_gk = knapSackEE(130, gk_start_cost_array, gk_points_array, len(gk_points_array), range(len(gk_points_array)), 2)
included_df = knapSackEE(350, df_start_cost_array, df_points_array, len(df_points_array), range(len(df_points_array)), 5)
included_mf = knapSackEE(600, mf_start_cost_array, mf_points_array, len(mf_points_array), range(len(mf_points_array)), 5)
included_fw = knapSackEE(350, fw_start_cost_array, fw_points_array, len(fw_points_array), range(len(fw_points_array)), 3)
print(included_gk)
gks_points = np.array([], dtype='i')
gks_cost = np.array([], dtype='i')

for i in range(len(included_gk)):
    if included_gk[i] == included_gk[i-1]:
        continue
    else:
        gks_cost = np.append(gks_cost,i)
        gks_points = np.append(gks_points,included_gk[i])
        
dfs_points = np.array([], dtype='i')
dfs_cost = np.array([], dtype='i')

for i in range(len(included_df)):
    if included_df[i] == included_df[i-1]:
        continue
    else:
        dfs_cost = np.append(dfs_cost,i)
        dfs_points = np.append(dfs_points,included_df[i])

mfs_points = np.array([], dtype='i')
mfs_cost = np.array([], dtype='i')

for i in range(len(included_mf)):
    if included_mf[i] == included_mf[i-1]:
        continue
    else:
        mfs_cost = np.append(mfs_cost,i)
        mfs_points = np.append(mfs_points,included_mf[i])
        
fws_points = np.array([], dtype='i')
fws_cost = np.array([], dtype='i')

for i in range(len(included_fw)):
    if included_fw[i] == included_fw[i-1]:
        continue
    else:
        fws_cost = np.append(fws_cost,i)
        fws_points = np.append(fws_points,included_fw[i])
m = np.array([[[[0 for x in range(len(fws_points))] for x in range(len(mfs_points))] for x in range(len(dfs_points))] for x in range(len(gks_points))])
for i in range(len(gks_points)):
    for j in range(len(dfs_points)):
        for k in range(len(mfs_points)):
            for l in range(len(fws_points)):
                if gks_cost[i] + dfs_cost[j] + mfs_cost[k] + fws_cost[l] > 1000:
                    continue
                else:
                    m[i][j][k][l] = gks_points[i] + dfs_points[j] + mfs_points[k] + fws_points[l]

max_value = np.amax(m)
print(max_value)
max_index = np.where(m == max_value)
gks_index = max_index[0]
dfs_index = max_index[1]
mfs_index = max_index[2]
fws_index = max_index[3]

gks_final_cost = gks_cost[gks_index]
dfs_final_cost = dfs_cost[dfs_index]
mfs_final_cost = mfs_cost[mfs_index]
fws_final_cost = fws_cost[fws_index]

selected_gk = knapSackE(int(gks_final_cost), gk_start_cost_array, gk_points_array, len(gk_points_array), range(len(gk_points_array)), 2)
selected_df = knapSackE(int(dfs_final_cost), df_start_cost_array, df_points_array, len(df_points_array), range(len(df_points_array)), 5)
selected_mf = knapSackE(int(mfs_final_cost), mf_start_cost_array, mf_points_array, len(mf_points_array), range(len(mf_points_array)), 5)
selected_fw = knapSackE(int(fws_final_cost), fw_start_cost_array, fw_points_array, len(fw_points_array), range(len(fw_points_array)), 3)

print(gk_name_array[selected_gk],df_name_array[selected_df],mf_name_array[selected_mf],fw_name_array[selected_fw])


