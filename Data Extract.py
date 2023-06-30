from urllib.request import urlopen
import json

link1 = str(input("Link:"))
filename = str(input("Filename:"))


f1 = urlopen(link1)
myfile1 = f1.read()
f = json.loads(myfile1)
#print(myfile)

with open(filename, "w") as file:
    json.dump(f,file,indent=2)
