# Define the Student class
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}  # Dictionary to store assignment names and grades

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}.")

    def display_grades(self):
        print(f"Grades for {self.name}:")
        if self.assignments:
            for assignment, grade in self.assignments.items():
                print(f"- {assignment}: {grade}")
        else:
            print("No assignments graded yet.")

# Define the Instructor class
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []  # List to store students

    def add_student(self, student):
        self.students.append(student)
        print(f"Added student {student.name} (ID: {student.student_id}) to the course '{self.course_name}'.")

    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student with ID {student_id} not found in the course.")

    def display_all_students_and_grades(self):
        print(f"\nAll students and their grades in '{self.course_name}':")
        if self.students:
            for student in self.students:
                print(f"\n{student.name} (ID: {student.student_id})")
                student.display_grades()
        else:
            print("No students enrolled in the course.")

# Initialize an instructor
instructor = Instructor("Dr. Smith", "Computer Science 101")

# Interactive flow for adding students and assigning grades
def instructor_flow():
    while True:
        action = input("\nEnter 'add student' to add a student, 'assign grade' to assign a grade, 'display' to view all students and grades, or 'exit' to quit: ").strip().lower()
        if action == "add student":
            student_name = input("Enter the student's name: ").strip()
            student_id = input("Enter the student's ID: ").strip()
            student = Student(student_name, student_id)
            instructor.add_student(student)
        elif action == "assign grade":
            student_id = input("Enter the student's ID: ").strip()
            assignment_name = input("Enter the assignment name: ").strip()
            try:
                grade = float(input("Enter the grade: ").strip())
                instructor.assign_grade(student_id, assignment_name, grade)
            except ValueError:
                print("Invalid grade. Please enter a numeric value.")
        elif action == "display":
            instructor.display_all_students_and_grades()
        elif action == "exit":
            print("Exiting the course management system.")
            break
        else:
            print("Invalid action. Please try again.")

# Run the interactive flow
instructor_flow()
