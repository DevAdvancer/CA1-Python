# Write a program in Python to find the roots of Quadratic equation.
import cmath

def find_roots(a, b, c):
    d = (b**2) - (4*a*c)

    root1 = (-b-cmath.sqrt(d))/(2*a)
    root2 = (-b+cmath.sqrt(d))/(2*a)

    return root1, root2

a = float(input('Enter a: '))
b = float(input('Enter b: '))
c = float(input('Enter c: '))

root1, root2 = find_roots(a, b, c)

print('The roots are {0} and {1}'.format(root1, root2))
