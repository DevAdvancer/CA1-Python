# Write a Python program to find the average of n numbers using list.
n = int(input("Enter the number of elements: "))
numbers = []
for i in range(n):
    num = float(input("Enter number {}: ".format(i+1)))
    numbers.append(num)
average = sum(numbers)/n
print("The average of the numbers is: ", average)
