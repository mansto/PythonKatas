# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

def getFirstAndLastElementFromList(list):
   return [list[0], list[-1]]

list = [5, 10, 15, 20, 25]
newList = getFirstAndLastElementFromList(list)

print(f"List Count (should be 2): {len(newList)}")
print(f"First element (should be 5): {newList[0]}")
print(f"Last element (should be 25) {newList[-1]}")