
"""
    WAP to count the number of each character present in a string using the concept of a dictionary.
"""

s = input('Enter a string: ')

mp = {x: s.count(x) for x in s}

for (ch, freq) in mp.items():
    print(f"{ch} : {freq}")

