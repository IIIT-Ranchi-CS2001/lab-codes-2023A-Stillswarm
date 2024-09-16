
"""
    Write a python script to print the multiplication table of a given number up
    to the specified limit using a for loop.
"""

n = int(input("Enter a number: "))
r = int(input("Enter range: "))

for i in range(1, r + 1):
    print(f"{n} x {i} = {n * i}")

