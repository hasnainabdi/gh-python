def calculate(num1=None, operation=None, num2=None):
    """
    Performs a calculation based on user inputs or default parameters.

    :param num1: First number (default is None, prompting user input if not provided).
    :param operation: Operation to perform (+, -, *, /) (default is None).
    :param num2: Second number (default is None, prompting user input if not provided).
    """
    try:
        # Use default parameters or prompt the user
        if num1 is None:
            num1 = float(input("Enter your first number: "))
        if operation is None:
            operation = input("Enter the operation (+, -, *, /): ")
        if num2 is None:
            num2 = float(input("Enter your second number: "))

        # Perform the calculation based on the operation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero is undefined."
        else:
            result = "Invalid operation. Please use +, -, *, or /."

        # Display the result
        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")

# Example usage with default parameters
calculate()