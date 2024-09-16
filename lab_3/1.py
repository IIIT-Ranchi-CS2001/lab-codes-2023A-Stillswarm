"""
    Write a python script to find the squares of first n natural numbers. Display both the number and the
    square as shown below. Use while loop
                      Number    	  Square
                        1              	1
                        2             	4
                        …		        …
                        n		       n^2

"""

n = int(input("Enter the value of n"))

print("Number       Square")
for i in range(1, n + 1):
    print(f"{i}              {i * i}")
