
"""
    for the given string s = "Ba Ba Black Sheep", determine the following using inbuilt functions:-
    a) length of s
    b) first occurrence of s
    c) total occurrences of the letter 'a'
    d) Generate "Ta Ta Black Sheep"
"""
s = "Ba Ba Black Sheep"

#length of string
print("Length: ", len(s))

#first occurence of 'e'
print(s.find('e'))

#total no. of occurences of 'a'
print(s.count('a'))

#replace "Ba" with "Ta"
print(s.replace("Ba", "Ta"))