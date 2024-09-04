# Write a Python program to perform Linear search.
def linear_search(arr, x):
    return arr.index(x) if x in arr else -1

arr = [2, 3, 4, 10, 40]
x = 10
print(linear_search(arr, x))
