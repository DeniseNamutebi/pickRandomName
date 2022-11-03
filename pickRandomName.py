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


#This concatinates the names in the list
# print("The names list is " + " ".join(namesList))   

#This accepts mutiple inputs and assigns them individual variables
# name1, name2 = input('Enter the first names ').split()
# print('The names to pick from are ' + name1 + ' ' + name2)