import numpy as np
import json
from knapsack import knapSackE, knapSack, knapSackEE
from Players_against_strength import player_name_array, projected_points_array, gk_cost_array, gk_proj_points_array, df_cost_array, df_proj_points_array, mf_cost_array, mf_proj_points_array, fw_proj_points_array, fw_cost_array, gk_name_array, df_name_array, mf_name_array, fw_name_array


# gk_spaces = int(input("How many goalkeepers?"))
# df_spaces = int(input("How many defenders?"))
# mf_spaces = int(input("How many midfielders?"))
# fw_spaces = int(input("How many forwards?"))
# cost = int(input("How much in the bank? (100m is 1000)"))

gk_spaces = 2
df_spaces = 5
mf_spaces = 5
fw_spaces = 3
cost = 1000

included_gk = knapSackEE(130, gk_cost_array, gk_proj_points_array, len(gk_proj_points_array), range(len(gk_proj_points_array)),
                         gk_spaces)
included_df = knapSackEE(350, df_cost_array, df_proj_points_array, len(df_proj_points_array), range(len(df_proj_points_array)),
                         df_spaces)
included_mf = knapSackEE(600, mf_cost_array, mf_proj_points_array, len(mf_proj_points_array), range(len(mf_proj_points_array)),
                         mf_spaces)
included_fw = knapSackEE(350, fw_cost_array, fw_proj_points_array, len(fw_proj_points_array), range(len(fw_proj_points_array)),
                         fw_spaces)

gks_points = np.array([], dtype='f')
gks_cost = np.array([], dtype='i')

for i in range(len(included_gk)):
    if included_gk[i] == included_gk[i - 1]:
        continue
    else:
        gks_cost = np.append(gks_cost, i)
        gks_points = np.append(gks_points, included_gk[i])

dfs_points = np.array([], dtype='f')
dfs_cost = np.array([], dtype='i')

for i in range(len(included_df)):
    if included_df[i] == included_df[i - 1]:
        continue
    else:
        dfs_cost = np.append(dfs_cost, i)
        dfs_points = np.append(dfs_points, included_df[i])

mfs_points = np.array([], dtype='f')
mfs_cost = np.array([], dtype='i')

for i in range(len(included_mf)):
    if included_mf[i] == included_mf[i - 1]:
        continue
    else:
        mfs_cost = np.append(mfs_cost, i)
        mfs_points = np.append(mfs_points, included_mf[i])

fws_points = np.array([], dtype='f')
fws_cost = np.array([], dtype='i')

for i in range(len(included_fw)):
    if included_fw[i] == included_fw[i - 1]:
        continue
    else:
        fws_cost = np.append(fws_cost, i)
        fws_points = np.append(fws_points, included_fw[i])
m = np.array(
    [[[[0 for x in range(len(fws_points))] for x in range(len(mfs_points))] for x in range(len(dfs_points))] for x in
     range(len(gks_points))],dtype='f')
for i in range(len(gks_points)):
    for j in range(len(dfs_points)):
        for k in range(len(mfs_points)):
            for l in range(len(fws_points)):
                if gks_cost[i] + dfs_cost[j] + mfs_cost[k] + fws_cost[l] > cost:
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

selected_gk = knapSackE(int(gks_final_cost), gk_cost_array, gk_proj_points_array, len(gk_proj_points_array),
                        range(len(gk_proj_points_array)), gk_spaces)
selected_df = knapSackE(int(dfs_final_cost), df_cost_array, df_proj_points_array, len(df_proj_points_array),
                        range(len(df_proj_points_array)), df_spaces)
selected_mf = knapSackE(int(mfs_final_cost), mf_cost_array, mf_proj_points_array, len(mf_proj_points_array),
                        range(len(mf_proj_points_array)), mf_spaces)
selected_fw = knapSackE(int(fws_final_cost), fw_cost_array, fw_proj_points_array, len(fw_proj_points_array),
                        range(len(fw_proj_points_array)), fw_spaces)

print(gk_name_array[selected_gk], df_name_array[selected_df], mf_name_array[selected_mf], fw_name_array[selected_fw])
print(gk_proj_points_array[selected_gk], df_proj_points_array[selected_df], mf_proj_points_array[selected_mf], fw_proj_points_array[selected_fw])
