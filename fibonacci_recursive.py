# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def CheckInputIsValid(input):
    number = 0

    try:
        number = int(input)
    except:
        raise ValueError(f"{input} is not a valid number")

    if number < 1 or number > 500:
        raise ValueError(f"{input} must be between 0 and 500")


def Fibonacci(n):
    if n < 0:
        raise ValueError("Invalid input")

    if n == 0:
        return 0

    if n == 1:
        return 1

    return Fibonacci(n-1) + Fibonacci(n-2)

input = input("How many fibonacci numbers should be generated?: ")
CheckInputIsValid(input)

for i in range(int(input)):
    print(Fibonacci(i+1), end = ", ")