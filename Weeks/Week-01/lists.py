#

operators = ("+", "-", "*", "/")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Choose an operator (+, -, *, /): ")

if op in operators:
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    print("Result:", result)
else:
    print("Invalid operator")