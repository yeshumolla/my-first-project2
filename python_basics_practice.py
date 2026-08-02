# ==========================================
# 1. Lambda Functions (አጫጭር/ወዲያውኑ የሚሰሩ ፋንክሽኖች)
# ==========================================

print("--- Lambda Functions Examples ---")

# Simple lambda function (ለቀረበው ቁጥር 20 ይጨምራል)
add_twenty = lambda y: y + 20
print("1. Add 20:", add_twenty(10))

# Multiply three numbers (ሶስት ቁጥሮችን ማበዛት)
multiply = lambda x, y, z: x * y * z
print("2. Multiply 5 * 5 * 5:", multiply(5, 5, 5))

# Addition of three numbers (ሶስት ቁጥሮችን መደመር)
add_three = lambda x, y, z: x + y + z
print("3. Addition 5 + 5 + 5:", add_three(5, 5, 5))

# Division of three numbers (ሶስት ቁጥሮችን ማካፈል)
divide = lambda x, y, z: x / y / z
print("4. Division 100 / 5 / 4:", divide(100, 5, 4))


# ==========================================
# 2. Higher-Order Function (ላምብዳ በፋንክሽን ውስጥ)
# ==========================================

print("\n--- Lambda inside a Function ---")

def multiplier_builder(x):
    """ይህ ፋንክሽን ሌላ አባዢ (Multiplier) ፋንክሽን ይፈጥራል።"""
    return lambda y: x * y

# የ 3 አባዢ ይፈጠራል
multiply_by_three = multiplier_builder(3)

print("Product 3 * 7:", multiply_by_three(7))
print("Product 3 * 10:", multiply_by_three(10))
print("Product 3 * 30:", multiply_by_three(30))


# ==========================================
# 3. Object-Oriented Programming (OOP)
# ==========================================

print("\n--- Student Class & Objects ---")

class Student:
    """የተማሪዎችን መረጃ የሚይዝ ክላስ"""
    
    def __init__(self, name: str, sex: str, department: str, age: int):
        """Constructor: ኦብጄክቱ ሲፈጠር መረጃዎችን ይቀበላል።"""
        self.name = name
        self.sex = sex
        self.department = department
        self.age = age

    def intro(self):
        """የተማሪውን መረጃ በግልጽ ያተማል (f-string በመጠቀም)።"""
        print(f"My name is {self.name}.")
        print(f"I am learning {self.department}.")
        print(f"I am {self.age} years old.")
        print("-" * 30)


# ኦብጄክቶችን መፍጠር (Creating Student Objects)
s1 = Student("Yeshambel", "male", "Software Engineering", 18)
s2 = Student("Afrata", "female", "Computer Science", 17)

# መረጃውን ማሳየት (Calling intro method)
s1.intro()
s2.intro()
