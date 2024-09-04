# Write a program in Python to check a triangle is equilateral,scalene or isosclees.
def check_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            return "Equilateral"
        elif a == b or a == c or b == c:
            return "Isosceles"
        else:
            return "Scalene"
    else:
        return "The sides cannot form a triangle"

a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))

print("The triangle is", check_triangle(a, b, c))
