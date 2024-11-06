# Part 1: https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
# Part 2: https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html
# Part 3: https://www.practicepython.org/exercise/2017/02/28/35-birthday-months.html
# Part 4: https://www.practicepython.org/exercise/2017/04/02/36-birthday-plots.html

import json
import datetime
from collections import Counter
from itertools import groupby

with open("dataFiles/birthdays.json", "r", encoding="utf-8") as file:
    birthday = json.load(file)

def list():
    print("We know the birthdays of:")
    for name in birthday:
        print(name)

def find():
    name = input("Who's birthday do you want to find: ")
    if name in birthday:
       print(f"{name}'s birthday is {birthday[name]}")
    else:
       print(f"Sorry, we don't know {name}")

def add():
    name = input("What is the name? ")
    bday = input("What is the birthday? (DD.MM.YYYY) ")
    birthday[name] = datetime.datetime.strptime(bday, "%d.%m.%Y").strftime("%d.%m.%Y")
    with open("dataFiles/birthdays.json", "w", encoding="utf-8") as file:
        json.dump(birthday, file)
    print("Birthday added.")

def groupByMonth():
    months = [datetime.datetime.strptime(birthday[name], "%d.%m.%Y").strftime("%B") for name in birthday]
    months.sort()
    c = Counter(months)
    for month, count in c.items():
        print(f"{month}: {count}")

def plot():
    print("Not implemented yet")

def main():
    while True:
        print()
        print("a. add")
        print("f. find")
        print("l. list")
        print("g. group by month")
        print("p. plot")
        print("q. Quit")
        print()

        action = input("What do you want to do? ").capitalize()

        if action.startswith("Q"):
            raise SystemExit(0)
        elif action.startswith("L"):
            list()
        elif action.startswith("F"):
            find()
        elif action.startswith("A"):
            add()
        elif action.startswith("G"):
            groupByMonth()
        elif action.startswith("P"):
            plot()

if __name__ == "__main__":
    main()