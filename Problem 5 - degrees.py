# math.degrees module
# Sara Hernandez
# November 5, 2022
# Convert radians to degrees


import math

radians = int(input("Enter a value in radians:"))

degrees = radians*180/math.pi

dif = degrees - math.degrees(radians)

print("The degree of the given radian is:", degrees)
print("The difference in the two methods is:", dif)


