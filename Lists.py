"""
    List in python
    -> insertion-order
    -> mutable
    -> different data types allowed(heterogeneous)

"""

""" ---CREATE A LIST--- """
list1 = []  # or list()
list2 = [1, 2, 3, 4]
list3 = ["apple", 4.5, True]
list4 = list("abhinav")  # ['a', 'b', 'h', .. ]
list5 = [-1] * 3  # [-1, -1, -1]

""" ---ADD ELEMENT(S)--- """
numbers = [15, 40, 63]

# insert()
numbers.insert(1, 45)   # insert 45 at index 1 (index compulsory)
numbers.append(45)  # adds 45 to the end of the list

# + operator
nums = [78, 96, 31]
numbers += nums  # append 'nums' to the end of 'numbers'

# extend()
numbers.extend({96, 55})    # argument must be an iterable
print(numbers)

""" ---REMOVE AN ELEMENT--- """
# remove()
numbers.remove(96)    # remove first occurrence of 96, return None
# numbers.remove(97)    # error - 97 not in list

# pop()
numbers.pop()   # removes the last element and returns it
x = numbers.pop(4)     # argument is index, must be in range, returns
print(numbers)

# clear()
# numbers.clear()   # removes all elements


""" ---LIST OPERATIONS--- """
# split()
s = "My name is Abhinav"
list6 = s.split()  # ['My', 'name', 'is', 'Abhinav']

str1 = "Tomorrow"
list7 = str1.split('r')  # ['Tomo', '', 'ow']

# join()
str2 = '+'.join(list6)  # My+name+is+Abhinav

# reverse a list
list8 = list6[::-1]  # ['Abhinav', 'is', 'name', 'My']
list6.reverse()  # returns None

# iterate using enumerate
for index, item in enumerate(list5):
    print(index, item)

# slicing (start inclusive, end exclusive)
sublist1 = list3[1:3]  # [4.5, True]
sublist2 = list3[1:100]  # [4.5, True]

""" ---SORTING--- """

# list.sort()
numbers.sort()  # ascending order, no return

# descending order
numbers.sort(reverse=True)

# sort strings by length
strs = ["apple", "banana", "kiwi", "pomegranate"]
strs.sort(key=len)
print(strs)

# sorted(list)
numbers_sorted = sorted(numbers)    # create and assign a new sorted list, original list doesn't change
print(numbers_sorted)
