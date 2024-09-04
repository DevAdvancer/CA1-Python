# Write a program in Python to print Reverse of a Number.
num = int(input("Enter a number: "))
reverse_num = 0
while num != 0:
    remainder = num % 10
    reverse_num = reverse_num * 10 + remainder
    num = num // 10
print("Reverse of the number is:", reverse_num)
