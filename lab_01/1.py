"""
    Write a program to find the:
    a. Sum,
    b. Difference,
    c. Product,
    d. Integer quotient,
    e. Remainder
    f. Fractional quotient
    of two numbers. Enter the numbers on run time. Display the
    input data and results in neat format.
"""

# input two numbers
a = float(input("Enter the first number(a): "))
b = float(input("Enter the second number(b): "))

# find sum
ans1 = a + b
print("a + b:", ans1)

# find subtraction
ans2 = a - b
print("a - b:", ans2)

# find multiplication
ans3 = a * b
print("a * b:", ans3)

# find integer quotient
ans4 = a // b
print("a // b:", ans4)

# find fractional quotient
ans5 = a / b
print("a / b:", ans5)

# find remainder
ans5 = a % b
print("a % b:", ans5)

