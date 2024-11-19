a = [x for x in range(10)]
print(a)

b = [x + 1 for x in range(10)]
print(b)

c = [x for x in range(10) if x % 2 == 0]
print(c)

options = ["any", "albany", "apple", "world", "hello", ""]
d = [x for x in options if len(x) > 0 and x[0] == 'a' and x[len(x) - 1] == 'y']
print(d)

# flatten a matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
e = [num for row in matrix for num in row]
print(e)

f = ["Even" if x % 2 == 0 else "Odd" for x in range(10)]
print(f)

# create a 2-d matrix
g = [[num for num in range(5)] for _ in range(5)]
print(g)


l3 = [[x * y for x in range(1, 4)] for y in range(1, 3)]  # [[1, 2, 3],[2, 4, 6]]
l4 = [[x * y] for x in range(1, 4) for y in range(1, 3)]  # [[1], [2], [2], [4], [3], [6]]
l5 = [x * y for x in range(1, 4) for y in range(1, 3)]  # [1, 2, 2, 4, 3, 6]
