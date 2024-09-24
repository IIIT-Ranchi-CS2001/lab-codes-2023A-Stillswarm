
"""
    Generate 2 lists (course code and course name). Create a new list with both
     course code and name like["CS1001:Python", ...]
"""

codes = list(input("Enter course codes: ").split())
names = list(input("Enter names: ").split())

ans = [x[0] + ": " + x[1] for x in zip(codes, names)]

print(ans)
