from urllib.request import urlopen
import numpy as np
import json

for j in range(1,3):
    link = "https://fantasy.premierleague.com/api/leagues-classic/132490/standings/?page_new_entries=1&page_standings=" + str(j) + "&phase=1"
    f = urlopen(link)
    myfile = f.read()
    y = json.loads(myfile)
    x = y['standings']
    z = x['results']
    for i in z:
        entry = i['entry']
        player_name = i['player_name']
        player_rank = i['rank']
        player_rank_sort = i['rank_sort']
        player_last_rank = i['last_rank']
        player_total = i['total']
        team_name = i['entry_name']
        linkentry = "https://fantasy.premierleague.com/api/entry/" + str(entry) + "/history/"
        f_entry = urlopen(linkentry)
        myfile_entry = f_entry.read()
        y_entry = json.loads(myfile_entry)
        x_entry = y_entry['chips']
        used_wildcard_1_ind = False
        used_wildcard_2_ind = False
        used_free_hit_ind = False
        used_triple_captain_ind = False
        used_bench_boost_ind = False
        for k in x_entry:
            if k['name']=='wildcard':
                if used_wildcard_1_ind == True:
                    used_wildcard_2_ind = True
                else:
                    used_wildcard_1_ind = True
            if k['name']=='free_hit':
                used_free_hit_ind = True
            if k['name']=='triple_captain':
                used_triple_captain_ind = True
            if k['name']=='bench_boost':
                used_bench_boost_ind = True
        print(str(player_rank) + " - " + player_name + " - " + team_name + " - " + str(player_total) + " - " + str(used_wildcard_1_ind))
