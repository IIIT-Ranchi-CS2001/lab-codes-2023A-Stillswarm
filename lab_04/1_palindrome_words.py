
"""
    Find the number of palindrome words in the given sentence without defining
     any new function (feel free to use python’s in-built functions).
"""

s = input("Enter a sentence: ")
s = s.lower()
words = s.split()

for word in words:
    if word == word[::-1]:
        print(word)