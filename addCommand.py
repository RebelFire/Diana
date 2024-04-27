import json
import datetime
from datetime import datetime
from datetime import timedelta

def LoadCommandsJson():
    f = open('commandsToRun.json')
    commandsData = json.load(f)
    return commandsData

def SaveCommandsJson():
    with open("commandsToRun.json", "w") as outfile:
        json.dump(commandsData, outfile)
    LoadCommandsJson



global commandsData
commandsData = LoadCommandsJson()




print("""
###########################
Eklenecek komut türünü seçiniz:
1- Sleep
2- Feed
3- Play
4- GiveWater
5- Hunt
###########################
""")



answer = input("")
if answer == "1":
    command = "sleep"
elif answer == "2":
    command = "feed"
elif answer == "3":
    command = "play"
elif answer == "4":
    command = "giveWater"
elif answer == "5":
    command = "hunt"
else:
    print("Invalid command")


timeX = datetime.now()
date_format = '%Y-%m-%d %H:%M:%S'

commandsData[len(commandsData)] = {'function': command, 'time': timeX.strftime(date_format)}

SaveCommandsJson()