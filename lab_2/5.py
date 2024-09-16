
"""
    Write a program to find the roots of a quadratic equation when the coefficients a, b, c are given.
"""
import math

a, b, c = input("Enter the coefficients: ").split()
a = int(a)
b = int(b)
c = int(c)

d = (b * b) - (4 * a * c)

root1, root2 = 0, 0

if d == 0:
    root1 = root2 = -b / (2 * a)
elif d > 0:
    root1 = (-b + math.sqrt(d)) / (2 * a)
    root2 = (-b - math.sqrt(d)) / (2 * a)
else:
    real_part = -b / (2 * a)
    imag_part = math.sqrt(-d / (2 * a))
    root1 = complex(real_part, imag_part)
    root2 = complex(real_part, -imag_part)

print("Roots are: ", root1, ", ", root2)