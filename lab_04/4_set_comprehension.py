
"""
    Generate two sets – first for all singers and second for all dancers
     of the class using set comprehension. Perform set operations to generate the following sets:
    a. of all artists of the class
    b. all-rounders of the class
    c. dancers but not singers
    d. singers but not dancers
    e. dancers but not singers cum singers but not dancers

"""

singers = set(input("Enter names of singers: ").split())
dancers = set(input("Enter names of dancers: ").split())

all = singers | dancers
print("All artists: ", all)

both = singers & dancers
print("All-rounders: ", both)

dancers_only = dancers - singers
print("Dancers but not singers: ", dancers_only)

singers_only = singers - dancers
print("Singers but not dancers: ", singers_only)

one = dancers_only | singers_only
print("Dancers but not singers and singers but not dancers: ", one)
