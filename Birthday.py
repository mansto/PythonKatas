# https://www.practicepython.org/exercise/2017/01/24/33-birthday-dictionaries.html

birthday = {
    "Hans Maier": "01/01/1990",
    "Lina Kohlmann": "02/02/1991",
    "Peter Müller": "03/03/1992",
    "Anna Schmidt": "04/04/1993",
    "Hans Schmidt": "05/05/1994",
    "Lia Schmidt": "06/06/1995",
    "Peter Hauenmüller": "07/07/1996",
}

print("Welcome to the birthday dictionary. We know the birthdays of:")  
for name in birthday:
    print(name)

print("Who's birthday do you want to look up?")
name = input()

if name in birthday:
    print(f"{name}'s birthday is {birthday[name]}")
else:
    print(f"Sorry, we don't know {name}")