# Write a Python program to check a number is palindrome or not.
def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
