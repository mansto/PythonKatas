# Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to the screen. 

def readFromFile():
    with open("dataFiles/readFromFile.txt") as file:
        return file.read().split("\n")

allNames = readFromFile()

result = {}

for name in allNames:
    amount = 1
    if name in result:
        amount = result[name] + 1

    result[name] = amount

for key in result:
    print(f"{key}: {result[key]}")