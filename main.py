import json
import time
import datetime
from datetime import datetime
from datetime import timedelta


statsFile = open('petStats.json')
global statsData 
statsData = json.load(statsFile)

commandsFile = open('commandsToRun.json')
global commands
commands = json.load(commandsFile)


startTimer = time.time()

def LoadStatsJson():
    global statsData
    f = open('petStats.json')
    statsData = json.load(f)

def SaveStatsJson():
    global statsData
    with open("petStats.json", "w") as outfile:
        json.dump(statsData, outfile)
    LoadStatsJson()

def LoadCommandsJson():
    global commands
    f = open('commandsToRun.json')
    commands = json.load(f)



def HandleCommand(command):
    if command == 'feed':
        Feed()
    elif command == 'play':
        Play()
    elif command == 'sleep':    
        Sleep()
    elif command == 'giveWater':
        GiveWater()
    elif command == 'hunt':
        Hunt()
    else:
        print('Invalid command')


def CheckFunctionTime(timeX):
    startTimer = datetime.now()
    date_format = '%Y-%m-%d %H:%M:%S'
    date_obj = datetime.strptime(timeX, date_format)
    if startTimer - date_obj < timedelta(minutes=1) and startTimer - date_obj > timedelta(seconds=0):
        return True
    return False

def CommandCheck():
    for key in commands:
        command = commands[key]['function']
        timeX = commands[key]['time']
        if CheckFunctionTime(timeX) == True:
            HandleCommand(command)


def PassTime():
    statsData['hunger'] = max(0, statsData['hunger'] - 1)
    statsData['thirst'] = max(0, statsData['thirst'] - 1)
    statsData['fun'] = max(0, statsData['fun'] - 1)


def Feed():
    statsData['hunger'] = min(1000, statsData['hunger']+ 250)

def Play():
    statsData['fun'] = min(1000, statsData['fun']+ 250)

def Sleep():
    statsData['health'] = min(100, statsData['health']+ 50)

def GiveWater():
    statsData['thirst'] = min(1000, statsData['thirst']+ 250)

def Hunt():
    statsData['health'] = max(0, statsData['health'] - 1)
    

while True:
    if time.time() - startTimer > 60:
        LoadCommandsJson()
        PassTime()
        CommandCheck()
        startTimer = time.time()
        SaveStatsJson()
        print("Time passed")
        print(statsData)
        
