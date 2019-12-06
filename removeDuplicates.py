# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

def removeDuplicates(input):
    return set(input) # In mathematics, a set is a collection of elements where no element is repeated.

input = [1,1,3,6,2,3,3,6,9,8,9,23,258,6]

result = removeDuplicates(input)
print(*result, sep=",")

