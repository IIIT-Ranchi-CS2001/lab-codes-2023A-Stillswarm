
"""
    Write a python script to print the first n terms of the Fibonacci series using while loop.

"""

n = int(input("Enter the number of terms of the Fibonacci series: "))

i, j = 0, 1
if n == 1:
    print(0)

else:
    print("0 1", end=" ")
    while i < n:
        k = i + j
        print(k, end=" ")
        i = j
        j = k

