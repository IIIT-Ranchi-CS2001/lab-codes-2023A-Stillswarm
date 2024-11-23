
"""
    Generate two tuples to represent two distinct points in space. (Three dimensional geometry). Determine the
    Euclidean distance between the two.
"""
import math
t1 = tuple([int(x) for x in input("Enter point 1: ").split()])
t2 = tuple([int(x) for x in input("Enter point 2: ").split()])

dist = 0
for x in zip(t1, t2):
    diff = x[0] - x[1]
    dist += diff * diff

dist = math.sqrt(dist)
print(dist)
