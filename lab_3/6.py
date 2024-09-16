"""
    Write a python script to find the number of occurrences of a particular
    character present in the given string using a loop. (Don’t use string methods).
"""

s = input('Enter a string: ')
ch = input("Enter a character: ")

ct = 0
for c in s:
    if c == ch:
        ct += 1

print("No. of occurrences: ", ct)
