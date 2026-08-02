# ==========================================================
# Real-World Project: Student Management System
# Features: Object-Oriented Programming (OOP) & Lambda Expressions
# ==========================================================

class Student:
    """የተማሪን መረጃ የሚያቀናጅ ክላስ (OOP Blueprint)"""
    def __init__(self, student_id: int, name: str, department: str, age: int, gpa: float):
        self.student_id = student_id
        self.name = name
        self.department = department
        self.age = age
        self.gpa = gpa

    def display_info(self):
        """የተማሪውን ሙሉ መረጃ በግልጽ ያሳያል"""
        print(f"🆔 ID: {self.student_id} | 👤 Name: {self.name} | 📚 Dept: {self.department} | 🎂 Age: {self.age} | 🎯 GPA: {self.gpa}")


class StudentDatabase:
    """የተማሪዎችን ዳታቤዝ የሚያስተዳድር ክላስ"""
    def __init__(self):
        self.students = []

    def add_student(self, student: Student):
        """አዲስ ተማሪ ወደ ሲስተሙ ይጨምራል"""
        self.students.append(student)
        print(f"✅ Student '{student.name}' added successfully!")

    def show_all_students(self):
        """የሁሉንም ተማሪዎች ዝርዝር ያሳያል"""
        print("\n--- 📋 ALL REGISTERED STUDENTS ---")
        if not self.students:
            print("No students registered yet.")
            return
        for s in self.students:
            s.display_info()

    def sort_students_by_age(self):
        """ተማሪዎችን በዕድሜ ለማደራጀት Lambda Function ይጠቀማል"""
        # Lambda function ን በመጠቀም በ 'age' መደርደር
        sorted_list = sorted(self.students, key=lambda s: s.age)
        print("\n--- 🎂 STUDENTS SORTED BY AGE (Youngest to Oldest) ---")
        for s in sorted_list:
            s.display_info()

    def filter_adult_students(self):
        """ዕድሜያቸው 18 እና ከዚያ በላይ የሆኑትን ለመለየት Lambda ይጠቀማል"""
        # Lambda function ን በመጠቀም ከ 18 በላይ የሆኑትን ብቻ መለየት
        adults = list(filter(lambda s: s.age >= 18, self.students))
        print("\n--- 🎓 ADULT STUDENTS (Age 18+) ---")
        for s in adults:
            s.display_info()


# ==========================================================
# Execution (ፕሮግራሙን ማስኬጃ)
# ==========================================================

if __name__ == "__main__":
    # ሲስተሙን መክፈት
    db = StudentDatabase()

    # አዳዲስ ተማሪዎችን መመዝገብ (Creating Objects)
    s1 = Student(101, "Yeshambel", "Software Engineering", 18, 3.8)
    s2 = Student(102, "Afrata", "Computer Science", 17, 3.9)
    s3 = Student(103, "Dawit", "Information Technology", 20, 3.5)
    s4 = Student(104, "Mena", "Cyber Security", 16, 3.7)

    # ተማሪዎችን ወደ ዳታቤዝ ማስገባት
    print("--- 📥 REGISTERING STUDENTS ---")
    db.add_student(s1)
    db.add_student(s2)
    db.add_student(s3)
    db.add_student(s4)

    # 1. ሁሉንም ተማሪዎች ማሳየት
    db.show_all_students()

    # 2. በዕድሜ ደርድሮ ማሳየት (Using Lambda)
    db.sort_students_by_age()

    # 3. ከ 18 ዓመት በላይ የሆኑትን ብቻ ማሳየት (Using Lambda Filter)
    db.filter_adult_students()
      
