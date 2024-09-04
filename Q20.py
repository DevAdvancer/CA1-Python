# Write a program in Python to print Factors of a Number.
def print_factors(num):
    factors = [i for i in range(1, num + 1) if num % i == 0]
    return factors

num = int(input("Enter a number: "))
print("The factors of", num, "are:", print_factors(num))
