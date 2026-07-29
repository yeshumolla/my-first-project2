# ==========================================
# Simple Python Calculator Project
# Topics Covered: Functions, User Input, Loops, If-Else
# ==========================================

# 1. Math Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

# 2. Main Program Function
def run_calculator():
    print("====================================")
    print("     Welcome to Python Calculator   ")
    print("====================================")
    
    while True:
        print("\nSelect Operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit (ለማቆም)")
        
        choice = input("Enter choice (1-5): ")
        
        # exit option
        if choice == '5':
            print("Thank you for using the calculator! Goodbye!")
            break
            
        # Check if the choice is valid
        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print(f"Result: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input! Please select a valid option.")

# Run the calculator
run_calculator()
           
