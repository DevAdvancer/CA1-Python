# Write a program in Python to find the area of a circle.
import math

def find_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    area = math.pi * (radius ** 2)
    return area

radius = float(input("Enter the radius of the circle: "))
area = find_circle_area(radius)

print(f"The area of the circle with radius {radius} is {area:.2f}")
