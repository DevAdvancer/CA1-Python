# Write a program in Python to print sum of natural number.

def sum_of_natural_numbers(n):
    return n * (n + 1) // 2

n = int(input("Enter a natural number: "))
print("Sum of natural numbers up to", n, "is:", sum_of_natural_numbers(n))

def sum_of_natural_numbers_for_loop(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = int(input("Enter a natural number: "))
print("Sum of natural numbers up to", n, "is:", sum_of_natural_numbers_for_loop(n))

def sum_of_natural_numbers_recursion(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_natural_numbers_recursion(n - 1)

n = int(input("Enter a natural number: "))
print("Sum of natural numbers up to", n, "is:", sum_of_natural_numbers_recursion(n))
