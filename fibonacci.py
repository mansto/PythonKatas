# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def CheckInputIsValid(input):
    result = 0

    try:
        result = int(input)
    except:
        raise ValueError(f"{input} is not a valid number")

    if result < 1 or result > 500:
        raise ValueError(f"{input} must be between 0 and 500")


def GenrateFibonacciSequence(amount):

    i = 1

    if amount == 0:
        result = []
    elif amount == 1:
        result = [1]
    elif amount == 2:
        result = [1,1]
    else:
        result = [1, 1]

    while i < amount -1:
        result.append(result[i] + result[i-1])
        i += 1

    return result

input = input("How many fibonacci numbers should be generated?: ")
CheckInputIsValid(input)
sequence = GenrateFibonacciSequence(int(input))
print(*sequence, sep = ", ")