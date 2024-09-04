# Write a program in Python to swap two numbers without using third variable

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Before swapping:")
print("Number 1:", num1)
print("Number 2:", num2)

num1, num2 = num2, num1

print("After swapping:")
print("Number 1:", num1)
print("Number 2:", num2)
