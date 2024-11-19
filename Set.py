
"""
    SETS IN PYTHON:
    -> unordered
    -> unique elements
    -> mutable
    -> O(1) search complexity
"""

""" ---CREATE A SET--- """
s1 = {}
s2 = set()
s3 = {1, 4.36987, 5, 'apple', 1, 5, 5}  # {1, 4, 5, 6}

""" ---TRAVERSING A SET--- """
# only for/in or enumerate as set object is not subscriptable

""" ---ACCESS SET ELEMENTS--- """
# set elements cannot be accessed by indexing or slicing
# also, concatenation(+) and repetition(*) operators do not work on sets

""" ---INSERT ELEMENTS--- """
s3.add(8)   # {1, 4.36987, 5, 'apple', 8}
s3.update([8, 2])   # {1, 2, 4.36987, 5, 'apple', 8}

""" ---REMOVE ELEMENTS--- """
s3.remove(8)    # known element - removes
# s3.remove(9)    # unknown element - throws error

s3.discard(1)   # known element - removes
s3.discard(100)   # unknown element - does nothing

x = s3.pop()    # removes a random element and returns it

""" ---SET BINARY OPERATIONS--- """
s4 = {1, 2, 3}
s5 = {2, 3, 4}
o1 = s4 & s5    # alternatively, use s4.intersection(s5)
o2 = s4 | s5    # elements present in both
o3 = s4 - s5    # elements of s4 not present in s5
o4 = s4 ^ s5    # either set but not it both
print(o1, " ", o2, " ", " ", o3, " ", o4)

""" ---RELATE TWO SETS--- """
print(s4.issuperset(s5))    # is s4 superset of s5?
print(s4.issubset(s5))  # is s4 subset of s5?
print(s4.isdisjoint(s5))    # is s4 intersection s5 = empty
