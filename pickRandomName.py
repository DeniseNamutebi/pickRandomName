import random
import time
import sys

namesList = []
def createNamesList():
    print("Enter your the names of each person")
    while True: 
        line = input()
        if line: 
            namesList.append(line)
        else: 
            break

def randomName(names):
    randomIndex = random.randint(0,len(names)-1)
    print("The name picked is ")
    anticipation = "..."
    for x in anticipation:
        print (x, end=" ", flush=True),
        #sys.stdout.flush()
        time.sleep(1)
    return print(names[randomIndex])


createNamesList()
print("\n")
randomName(namesList)
