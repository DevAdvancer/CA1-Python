# Write a program in Python to find given no is Even or Odd.
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

num = int(input("Enter a number: "))
print(check_even_odd(num))
