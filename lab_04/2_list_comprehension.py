
"""
    List Comprehension: Create a list of int using list comprehension [multiple input from keyboard].
    Find the mean, median, and mode of the given list (usage of specific modules such as statistics is not allowed.
    Lab problems are for you to build-up logic and strengthen your understanding of the topic & its concepts).

"""

lst = list(map(int, input("Enter some numbers: ").split()))

lst.sort()

n = len(lst)

sum = 0
mx = 0
for i in lst:
    sum += i
    mx = max(mx, i)

print("Mean: ", sum / n)

if len(lst) % 2 == 0:
    print(f"Medians: {lst[n // 2 - 1]}, {lst[n // 2]}")
else:
    print("Median: ", lst[n // 2])

mp = {lst.count(x): x for x in lst}

print("Mode: ", mp[max(mp)])
