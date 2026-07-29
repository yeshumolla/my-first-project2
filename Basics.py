# ==========================================
# First Python Practice Script
# Topics Learned: Functions, Loops, Arguments
# ==========================================

# 1. Function to greet the user
def greet_user(name):
    print("Welcome to my Python script, " + name + "!")

# 2. Function for addition
def add_numbers(num1, num2):
    return num1 + num2

# 3. Function for multiplication
def multiply_numbers(num1, num2):
    return num1 * num2

# 4. Function to count numbers by steps using a loop
def count_by_step(start, stop, step):
    print(f"Counting from {start} to {stop} by {step}:")
    for i in range(start, stop + 1, step):
        print(i)

# 5. Function to sum numbers in a range
def calculate_total_sum(limit):
    total = 0
    for i in range(limit + 1):
        total += i
    return total


# ==========================================
# Running the Program (Execution)
# ==========================================

greet_user("Developer")

print("\n--- Math Operations ---")
print("Addition Result (25 + 25):", add_numbers(25, 25))
print("Multiplication Result (5 * 5):", multiply_numbers(5, 5))

print("\n--- Loop Operations ---")
count_by_step(5, 50, 5)

print("\n--- Total Sum ---")
print("Sum of 0 to 100 is:", calculate_total_sum(100))
