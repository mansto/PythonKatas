# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

import json

with open("dataFiles/birthdays.json", "r", encoding="utf-8") as file:
    birthday = json.load(file)

def listNames():
    print("We know the birthdays of:")
    for name in birthday:
        print(name)

def findAndPrintBirthDay():
    name = input("Who's bithday do you want to find: ")
    if name in birthday:
       print(f"{name}'s birthday is {birthday[name]}")
    else:
       print(f"Sorry, we don't know {name}")

def addBirthday():
    name = input("What is the name? ")
    bday = input("What is the birthday? ")
    birthday[name] = bday
    with open("dataFiles/birthdays.json", "w", encoding="utf-8") as file:
        json.dump(birthday, file)
    print("Birthday added.")

while True:

    action = input("What do you want to do? Possible actions are: (A)dd, (F)ind, (L)ist or (Q)uit\n").capitalize()

    if action.startswith("Q"):
        raise SystemExit(0)
    elif action.startswith("L"):
        listNames()
    elif action.startswith("F"):
        findAndPrintBirthDay()
    elif action.startswith("A"):
        addBirthday()