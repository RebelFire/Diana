import datetime
from datetime import datetime
import time
import petCommands

#   Read json file every minute
#   Json files: commandsToRun.json, petStats.json, 
#   Python files: timer.py, petCommands.py, fileReader.py, commands.py, petStats.py



startTimer = time.time()

while True:
    if time.time() - startTimer > 60:
        petCommands.Check()
        print(time.time())
        startTimer = time.time()