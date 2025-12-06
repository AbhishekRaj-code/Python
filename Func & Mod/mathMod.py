# imorting the math module to use mathematical functions
import math

#Taking input from the user
num = int(input("Enter a number: "))

#Using some functions from the math module
sqrt = math.sqrt(num)
nat_log = math.log(num)
sin = math.sin(num)

#Displaying the results
print(f"The square root of {num} is {sqrt}")
print(f"The natural logarithm of {num} is {nat_log}")
print(f"The sine of {num} (in radians) is {sin}")
