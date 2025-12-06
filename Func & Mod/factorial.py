# Factorial calculation using a function
def factorial(n):
    """Return the factorial of an integer n."""
    if n < 0:
        print("Factorial is not defined for negative numbers.")
        return None
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Taking user input and displaying the factorial
num = int(input("Enter a non-negative integer: "))
print(f"The factorial of {num} is {factorial(num)}")
