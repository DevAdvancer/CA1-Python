# Write a Python program to check a number is Armstrong or not.
def is_armstrong(num):
    num_str = str(num)
    num_len = len(num_str)
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len
    return sum == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
