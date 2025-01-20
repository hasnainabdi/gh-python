def calculate():
    
### I CREATED A ASSINGMENT OF GOVERNOR HOUSE. I CREATED CALCULATOR USE FUNCTIONS TO CREATE ADDITION, SUBTRACTION, MULTIPICATION AND DIVISION BASED FUNCTIONS. (DYNAMIC FUNCTION)
    
    try:
        # Get input from the user
        num1 = float(input("Enter your first number: "))
        operation = input("Enter the operation (+, -, *, /): ")
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

# Call the function to execute the program
calculate()

#© Copyright by Syed Muhammad Hasnain Abdi