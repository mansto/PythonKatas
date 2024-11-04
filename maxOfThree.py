# Implement a function that takes as input three variables, 
# and returns the largest of the three. 
# Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python normally takes care of for us. 
# All you need is some variables and if statements!

# https://www.practicepython.org/exercise/2016/03/27/28-max-of-three.html

def getLargestNumber(one, two, three):
    if one > two and one > three:
        return one
    elif two > one and two > three:
        return two
    else:
        return three

one = input("Enter the first number: ")
two = input("Enter the second number: ")
three = input("Enter the third number: ")

largestNumber = getLargestNumber(one, two, three)
print(f"The largest number is: {largestNumber}")





