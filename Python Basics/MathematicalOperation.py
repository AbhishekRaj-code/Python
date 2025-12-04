# Taking two numbers as input from the user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Performing basic mathematical operations
addition = num1 + num2  
subtraction = num1 - num2
multiplication = num1 * num2
division = round(num1 / num2,2) if num2 != 0 else print("Error: Division by zero is not allowed.")

# Displaying the results
print(f"Addition: {num1} + {num2} = {addition}")
print(f"Subtraction: {num1} - {num2} = {subtraction}")
print(f"Multiplication: {num1} * {num2} = {multiplication}")
print(f"Division: {num1} / {num2} = {division}")    

