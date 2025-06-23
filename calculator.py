num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operators = input("Enter the operators you want to use (e.g., +, -, *, /) ")

if operators == "+":
    result = num1 + num2
    print(round(result, 3))
elif operators == "-":
    result = num1 - num2
    print(round(result, 3))
elif operators == "*":
    result = num1 * num2
    print(round(result, 3))
elif operators == "/":
    if num2 != 0:
        result = num1 / num2
        print(round(result, 3))
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")