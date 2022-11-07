# math factorial module
# Sara Hernandez
# November 5, 2022
# use for loop to compute the factorial of a user input value


import math

num = int(input("Enter a number:"))

fac = 1

for i in range (1, num + 1):
    fac = fac * i

num1 = math.factorial(i)

print("The factorial of", num, "is", fac)
print(num1)
