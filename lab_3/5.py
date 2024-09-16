"""
    Write a python script to check whether all the characters present in a string
     are alphanumeric (uppercase letters, lowercase letters or digits) using for loop.
    Print True if all characters are alphanumeric, otherwise print False.
"""
import sys

s = input("Enter a string: ")

for i in s:
    if not i.isalnum():
        print(False)
        sys.exit()

print(True)