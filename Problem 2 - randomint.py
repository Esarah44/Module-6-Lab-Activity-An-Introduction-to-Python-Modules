# random.randint
# Sara Hernandez
# November 5, 2022
# This program uses random.randint to print an odd integer between 0 and 100


import random

OddNumber = random.randint(0,100)
OddNumber = (OddNumber // 2) - 1
OddNumber = (OddNumber * 2) + 1

print(OddNumber)

#another way
#while True:
#    num = random.randint(0, 100)
#    if num % 2 != 0:
#        break
#print("Odd number is", num)
