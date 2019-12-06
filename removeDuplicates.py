# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def removeDuplicates(input):
    return set(input) # In mathematics, a set is a collection of elements where no element is repeated.

inputNumbers = [1,1,3,6,2,3,3,6,9,8,9,23,258,6]
resultNumbers = removeDuplicates(inputNumbers)
print(*resultNumbers, sep=",")

inputStrings = ["a", "a", "b", "c", "a", "A"]
resultStrings = removeDuplicates(inputStrings)
print(*resultStrings, sep=",")

