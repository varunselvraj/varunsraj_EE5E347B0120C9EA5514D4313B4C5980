class Student:
    def _init_(self, name, roll_number, cgpa):
        self.name = name
        self.roll_number = roll_number
        self.cgpa = cgpa

def sort_students(student_list):
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage
# Creating student objects
student1 = Student("Alice", "001", 3.9)
student2 = Student("Bob", "002", 3.7)
student3 = Student("Charlie", "003", 4.0)
student4 = Student("David", "004", 3.5)

# List of student objects
students = [student1, student2, student3, student4]

# Sorting students based on CGPA
sorted_students = sort_students(students)

# Printing sorted students
print("Sorted Students based on CGPA:")
for student in sorted_students:
    print(f"Name: {student.name}, Roll Number: {student.roll_number}, CGPA: {student.cgpa}")