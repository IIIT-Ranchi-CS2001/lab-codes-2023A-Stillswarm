
"""
    Tuples in python:
    -> Ordered(indexed)
    -> heterogeneous
    -> immutable
    -> can contain mutable elements
    -> Indexed-access(tuple[0]) and slicing(tuple[0:3]) work the same as lists.

    -> Faster than list due to immutability
    -> provide data integrity
"""

""" ---CREATE A TUPLE--- """
t1 = ()
t2 = (1, "apple", 54.2, False)
t3 = 1e-7, 42, 'banana' # this is known as packing
t4 = tuple("Abhinav")   # ('A', 'b', 'h', 'i', 'n', 'a', 'v')
t5 = ([1, 2], (3, 4))
t5[0][0] = 2    # fine
# t5[1][0] = 100  # error - tuple does not support item assignment

""" ---ITERATING A TUPLE--- """
# works the same as lists.
# Iterate using len(), range(), for/in or enumerate

""" ---OPERATIONS ON TUPLES--- """
# swap numbers
a = 20
b = 30
a, b = b, a
print(a, " ", b)
a, b, c = 5, 10, 15     # this is known as unpacking
a, b, c = c, a, b

# partition() on string
t6 = "tomorrow".partition('rr')  # ('tomo', 'rr', 'ow') -> tuple of exactly three items

""" ---PACKING AND UNPACKING--- """
x, y, z = t3    # x = 1e-7, y = 42, z = banana

t7 = 10, 20, t3, 30     # (10, 20, (1e-07, 42, 'banana'), 30)
t8 = 10, 20, *t3, 30    # (10, 20, 1e-07, 42, 'banana', 30)
