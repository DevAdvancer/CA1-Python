# Write a program in Python to find the volume of a sphere with radius  6cm.
import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume

radius = 6
volume = calculate_sphere_volume(radius)

print(f"The volume of the sphere with radius {radius} cm is {volume:.2f} cubic cm.")
