
"""
    Enter three lists using list comprehension: Customer name, Customer ID, and shopping points. Construct a list of
    tuples with and without using built-in function zip().
"""

l1 = [x for x in input("Enter customer names: ").split()]
l2 = [x for x in input("Enter customer IDs: ").split()]
l3 = [int(x) for x in input("Enter shopping points: ").split()]

lst_using_zip = [(x[0], x[1], x[2]) for x in zip(l1, l2, l3)]
print(lst_using_zip)

lst_without_zip = []
for i in range(0, len(l1)):
    lst_without_zip.append((l1[i], l2[i], l3[i]))

print(lst_without_zip)
