# Write a Python Program to find the gravitational force acting between two objects. [G=N*(m1*m2)/d^2]
import math

def gravitational_force(m1, m2, d):
    G = 6.674 * (10**-11)  # gravitational constant in m^3 kg^-1 s^-2
    return G * (m1 * m2) / (d**2)

def main():
    m1 = float(input("Enter the mass of the first object in kg: "))
    m2 = float(input("Enter the mass of the second object in kg: "))
    d = float(input("Enter the distance between the two objects in meters: "))

    force = gravitational_force(m1, m2, d)
    print(f"The gravitational force acting between the two objects is {force} N.")

if __name__ == "__main__":
    main()
