# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

import datetime

currentYear = datetime.datetime.now().year

name = input("What's your name? _")
age = input("How old are you? _")
year100 = (currentYear - int(age)) + 100

print(f"Hello {name}. You will be 100 years old in the year { year100 }.")