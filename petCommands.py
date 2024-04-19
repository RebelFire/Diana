import json
import time
from datetime import datetime
from datetime import timedelta

# Opening JSON file
f = open('commandsToRun.json')
 

data = json.load(f)
commands = data['commands']
commandsDict = {
    'commands' : {

    }
}

def HandleCommand(command):
    if command == 'feed':
        print('Feed your pet')
    elif command == 'play':
        print('Play with your pet')
    elif command == 'sleep':    
        print('Put your pet to sleep')
    elif command == 'giveWater':
        print('Give your pet water')
    else:
        print('Invalid command')


def CheckFunctionTime(timeX):
    startTimer = datetime.now()
    
    date_format = '%Y-%m-%d %H:%M:%S'

    date_obj = datetime.strptime(timeX, date_format)

    #print(startTimer.strftime("%Y-%m-%d %H:%M:%S")) 
    #14:04:00 -> 14:03:00 - 14:04:00
    if startTimer - date_obj < timedelta(minutes=1) and startTimer - date_obj > timedelta(seconds=0):
        return True
    return False

def Check():
    for key in data['commands']:
        command = data['commands'][key]['function']
        timeX = data['commands'][key]['time']
        if CheckFunctionTime(timeX) == True:
            HandleCommand(command)




