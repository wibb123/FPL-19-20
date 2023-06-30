from urllib.request import urlopen
import json

wildcardweeks = []
link1 = "https://fantasy.premierleague.com/api/entry/286334/history/"

f1 = urlopen(link1)
myfile1 = f1.read()
#print(myfile)
for j in range(1,3):
    print(j)
    link = "https://fantasy.premierleague.com/api/leagues-classic/314/standings/?page_new_entries=1&page_standings=" + str(j) + "&phase=1"
    f = urlopen(link)
    myfile = f.read()
    y = json.loads(myfile)
    x = y['standings']
    z = x['results']
    for i in z:
        entry = i['entry']
        linkentry = "https://fantasy.premierleague.com/api/entry/" + str(entry) + "/history/"
        f_entry = urlopen(linkentry)
        myfile_entry = f_entry.read()
        y_entry = json.loads(myfile_entry)
        x_entry = y_entry['chips']
        for i in x_entry:
            if i['name']=='wildcard':
                wildcardweeks.append(i['event'])

for i in range(1,21):
    print("Week: " +str(i) + " Number of wildcards played: " + str(wildcardweeks.count(i)))