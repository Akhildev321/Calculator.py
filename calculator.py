# OPERATION FUNCTIONS
def add(numbers):
    """Returns the sum of numbers"""
    return sum(numbers)

def subtract(numbers):
    """Subtracts all numbers from the first number"""
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def multiply(numbers):
    """Returns the product of numbers"""
    result = 1
    for num in numbers:
        result *= num
    return result

def divide(numbers):
    """Divides first number by all subsequent numbers"""
    try:
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                raise ZeroDivisionError
            result /= num
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"

# INPUT FUNCTIONS
def get_float_input(prompt):
    """Gets and validates a float number from user"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation_choice():
    """Gets and validates the operation choice"""
    while True:
        choice = input("Choose operation (1-5): ")
        if choice in ['1', '2', '3', '4', '5']:
            return choice
        print("Invalid choice. Please enter 1-5.")

def get_number_count():
    """Gets how many numbers to operate on (2-5)"""
    while True:
        try:
            count = int(input("How many numbers? (2-5): "))
            if 2 <= count <= 5:
                return count
            print("Please enter 2-5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# DISPLAY FUNCTIONS
def show_menu():
    """Displays the calculator menu"""
    print("\n" + "="*20)
    print("PYTHON CALCULATOR")
    print("="*20)
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Exit")
    print("="*20)

def show_result(operation, numbers, result):
    """Displays the calculation result"""
    ops = {'1': ' + ', '2': ' - ', '3': ' * ', '4': ' / '}
    op_symbol = ops.get(operation, ' ? ')
    equation = op_symbol.join(map(str, numbers))
    print(f"\nResult: {equation} = {result}\n")

# MAIN CALCULATOR FUNCTION
def run_calculator():
    """Main function to run the calculator"""
    print("\nWelcome to the Python Calculator!")
    print("You can operate on 2-5 numbers per calculation.")
    
    while True:
        show_menu()
        choice = get_operation_choice()
        
        # Exit condition
        if choice == '5':
            print("\nThank you for using the calculator. Goodbye!")
            break
        
        # Get numbers
        count = get_number_count()
        numbers = [get_float_input(f"Enter number {i+1}: ") for i in range(count)]
        
        # Perform calculation
        operations = {
            '1': add,
            '2': subtract,
            '3': multiply,
            '4': divide
        }
        
        result = operations[choice](numbers)
        show_result(choice, numbers, result)

# PROGRAM ENTRY POINT
if __name__ == "__main__":
    run_calculator()
