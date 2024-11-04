# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html
# https://www.practicepython.org/exercise/2017/02/06/34-birthday-json.html

import json

with open("dataFiles/birthdays.json", "r", encoding="utf-8") as file:
    birthday = json.load(file)

print("Welcome to the birthday dictionary. We know the birthdays of:")  
for name in birthday:
    print(name)

print("Who's birthday do you want to look up?")
name = input()

if name in birthday:
    print(f"{name}'s birthday is {birthday[name]}")
else:
    print(f"Sorry, we don't know {name}")
    print("Would you like to add it? (yes/no)")
    answer = input()
    if answer == "yes":
        print("What is the birthday?")
        bday = input()
        birthday[name] = bday
        with open("dataFiles/birthdays.json", "w", encoding="utf-8") as file:
            json.dump(birthday, file)
        print("Birthday added.")