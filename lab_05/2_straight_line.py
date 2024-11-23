
"""Enter the coordinates of two points on the cartesian plane (take user input using comprehension). Find the
equation of the straight line passing through these points. Hint: Eqn is (x-x1) = ((x1-x2)/(y1-y2)) (y-y1)

"""

t1 = tuple([int(x) for x in input("Enter point 1: ").split()])
t2 = tuple([int(x) for x in input("Enter point 2: ").split()])

slope = (t1[0] - t2[0]) / (t1[1] - t2[1])

line = f"x - {t1[0]} = {slope} (y - {t1[1]})"
print(line)
