import random

namesList = []
print("Enter your the names of each person")
while True: 
    line = input()
    if line: 
        namesList.append(line)
    else: 
        break
print("The names to choose from are")
for x in namesList: print(x)
randomIndex = random.randint(0,len(namesList)-1)
print("The person picked is " + namesList[randomIndex])


