
"""
    Write a python script to find the sum of the digits of the given number using a while loop.
     Display the number and the sum
"""

n = int(input("Enter a number: "))

ans = 0
while n > 0:
    ans += n % 10
    n = n // 10

print(ans)