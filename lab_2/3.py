
"""
    Write a program to enter any string at runtime and check whether it is a palindrome or not.
"""

import sys
str = input("Enter a string: ")

for i in range(0, len(str) // 2):
    if str[i] != str[-(i + 1)]:
        print("Not a palindrome")
        sys.exit()

print("Palindrome")