

"""
    if the given string s1 = "Maha Bharat", generate the following strings by manipulating s1
"""

str = "Maha Bharat"
n = len(str)

# mAHA bHARAT
for i in range(0, n):
    if 'a' <= str[i] <= 'z':
        print(str[i].upper(), end="")
    else:
        print(str[i].lower(), end="")

print()

# Bharat
spaceFound = False
s = ""
for i in range(0, n):
    if spaceFound:
        print(str[i], end="")
        s = s + str[i]
    if str[i] == ' ':
        spaceFound = True

print()

# BharatBharatBharat
for i in range(0, 3):
    print(s, end="")

print()

# Mera Bharat
print(str.replace("Maha", "Mera"))

# Mera Bharat Mahan
print(str.replace("Maha", "Mera") + " Mahan")
