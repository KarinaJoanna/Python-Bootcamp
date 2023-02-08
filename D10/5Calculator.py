# Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

# Dictonary for store the functions

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("Enter the first number: "))

# Loop for print the symbols of the operations
for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("Enter the second number: ")) # We put in here for better user experience
calculation_function = operations[operation_symbol] # This is the same as: calculation_function = operations["+"] etc.
answer = calculation_function(num1, num2) # This is the same as: answer = add(num1, num2) etc.
print(f"{num1} {operation_symbol} {num2} = {answer}")
