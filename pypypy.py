
names = ['a', 'b', 'c', 'd', 'e']
marks = [90, 45, 63, 78, 69]

d = {x: y for x, y in zip(names, marks)}
print(d)
sorted_d = {x: d.get(x) for x in sorted(d, key=d.get, reverse=True)}
print(sorted_d)
