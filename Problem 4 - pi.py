# math pi module
# Sara Hernandez
# November 6, 2022
# Calculate an approximation for pi using Leibniz’s formula

import math

pi=0
denom=1

for i in range(0, 100000):
    if i % 2 == 0:
        pi=pi+4/denom
    else:
        pi = pi - 4/denom
    denom = denom + 2

print("PI =", pi)

dif = pi - math.pi

print("The difference in the two methods is:", dif)


