# Calculator

from art import logo

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


def calculator():
    print(logo)
    # recursion function for when the user want to start a new calculation

    num1 = float(input("Enter the first number: "))

    # Loop for print the symbols of the operations
    for symbol in operations:
        print(symbol)

    # Ask the user if they want to continue using the calculator

    should_continue = True
    while should_continue:
        operation_symbol = input("Pick another operation: ")
        num2 = float(input("Enter the next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
            # should_continue = True
        else:
            should_continue = False

calculator()

