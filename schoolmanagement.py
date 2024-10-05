class SchoolManagementSystem:
    def __init__(self):
        self.students = {}
        self.teachers = {}

    def add_student(self, student_id, name):
        if student_id not in self.students:
            self.students[student_id] = name
            print(f"Student {name} added with ID {student_id}.")
        else:
            print("Student ID already exists.")

    def remove_student(self, student_id):
        if student_id in self.students:
            removed_student = self.students.pop(student_id)
            print(f"Removed student: {removed_student} (ID: {student_id})")
        else:
            print("Student ID not found.")

    def view_students(self):
        if not self.students:
            print("No students enrolled.")
        else:
            print("List of Students:")
            for student_id, name in self.students.items():
                print(f"ID: {student_id}, Name: {name}")

    def add_teacher(self, teacher_id, name):
        if teacher_id not in self.teachers:
            self.teachers[teacher_id] = name
            print(f"Teacher {name} added with ID {teacher_id}.")
        else:
            print("Teacher ID already exists.")

    def remove_teacher(self, teacher_id):
        if teacher_id in self.teachers:
            removed_teacher = self.teachers.pop(teacher_id)
            print(f"Removed teacher: {removed_teacher} (ID: {teacher_id})")
        else:
            print("Teacher ID not found.")

    def view_teachers(self):
        if not self.teachers:
            print("No teachers available.")
        else:
            print("List of Teachers:")
            for teacher_id, name in self.teachers.items():
                print(f"ID: {teacher_id}, Name: {name}")

    def menu(self):
        while True:
            print("\nSchool Management System")
            print("1. Add Student")
            print("2. Remove Student")
            print("3. View Students")
            print("4. Add Teacher")
            print("5. Remove Teacher")
            print("6. View Teachers")
            print("7. Exit")

            choice = input("Select an option (1-7): ")

            if choice == '1':
                student_id = input("Enter Student ID: ")
                name = input("Enter Student Name: ")
                self.add_student(student_id, name)

            elif choice == '2':
                student_id = input("Enter Student ID to remove: ")
                self.remove_student(student_id)

            elif choice == '3':
                self.view_students()

            elif choice == '4':
                teacher_id = input("Enter Teacher ID: ")
                name = input("Enter Teacher Name: ")
                self.add_teacher(teacher_id, name)

            elif choice == '5':
                teacher_id = input("Enter Teacher ID to remove: ")
                self.remove_teacher(teacher_id)

            elif choice == '6':
                self.view_teachers()

            elif choice == '7':
                print("Exiting the system. Goodbye!")
                break

            else:
                print("Invalid choice! Please try again.")

# Start the School Management System
if __name__ == "__main__":
    system = SchoolManagementSystem()
    system.menu()
