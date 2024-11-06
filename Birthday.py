# Part 1: https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
# Part 2: https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
# Part 3: https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html

import json
import datetime
from collections import Counter
from itertools import groupby

with open("dataFiles/birthdays.json", "r", encoding="utf-8") as file:
    birthday = json.load(file)

def listNames():
    print("We know the birthdays of:")
    for name in birthday:
        print(name)

def findAndPrintBirthDay():
    name = input("Who's birthday do you want to find: ")
    if name in birthday:
       print(f"{name}'s birthday is {birthday[name]}")
    else:
       print(f"Sorry, we don't know {name}")

def addBirthday():
    name = input("What is the name? ")
    bday = input("What is the birthday? (DD.MM.YYYY) ")
    birthday[name] = datetime.datetime.strptime(bday, "%d.%m.%Y").strftime("%d.%m.%Y")
    with open("dataFiles/birthdays.json", "w", encoding="utf-8") as file:
        json.dump(birthday, file)
    print("Birthday added.")

def listBirthdaysPerMonth():
    months = [datetime.datetime.strptime(birthday[name], "%d.%m.%Y").strftime("%B") for name in birthday]
    months.sort()
    for key, group in groupby(months):
        print(f"{key}: {len(list(group))}")

while True:

    action = input("What do you want to do? Possible actions are: (A)dd, (F)ind, (L)ist, List (b)irthdays per month, or (Q)uit\n").capitalize()

    if action.startswith("Q"):
        raise SystemExit(0)
    elif action.startswith("L"):
        listNames()
    elif action.startswith("F"):
        findAndPrintBirthDay()
    elif action.startswith("A"):
        addBirthday()
    elif action.startswith("B"):
        listBirthdaysPerMonth()
