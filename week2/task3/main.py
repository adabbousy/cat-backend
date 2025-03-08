import os

FILE_NAME = "students.csv"


class Student:
    students = []
    def __init__(self, name, subject, grade):
        self.name = name
        self.subject = subject
        self.grade = grade

    def display(self):
        print(f"{self.name} -> {self.subject}: {self.grade}")


def main():
    load_from_file(FILE_NAME)
    # Check if any data were loaded.
    if Student.students:
        print("Loaded student records from file.")
        view_students()
    else:
        print("No previous records found. Starting fresh.")

    print("\nEnter 'exit' to stop inputting students.")
    while True:
        # Take name, subject, and grade from user.
        name = input("\nEnter student name: ").title()
        if name.lower() == "exit":
            break

        subject = input("Enter subject: ").title()

        try:
            grade = int(input("Enter grade: "))
        except ValueError:
            print("Invalid grade. Grade must be a number.")
            continue

        add_student(name, subject, grade)

    choice = input("\nDo you want to update a grade? (yes/no): ").lower()
    if choice == "yes" or choice == "y":
        name = input("Enter student name: ").title()
        new_grade = int(input("Enter new grade: "))
        update_grade(name, new_grade)

    # Save updated data to file.
    save_to_file(FILE_NAME)


def add_student(name, subject, grade):
     Student.students.append(Student(name, subject, grade))
     print("Student added successfully!")


def save_to_file(file):
    """Saves student records to a file in CSV format."""
    with open(file, 'w') as f:
        for student in Student.students:
            f.write(f"{student.name},{student.subject},{student.grade}\n")


def load_from_file(file):
    """Loads student records from a file if it exists."""
    # Check if file exists.
    if not os.path.exists(file):
        return

    with open(file, 'r') as f:
        for line in f:
            student, subject, grade = line.strip().split(',')
            add_student(student, subject, int(grade))


def update_grade(name, new_grade):
    for student in Student.students:
        if student.name == name:
            student.grade = new_grade
            save_to_file(FILE_NAME)
            print("Grade updated successfully!")
            break
    else:
        print("Student not found.")


def view_students():
    """Displays all student records."""
    print("\nStudent Records:")
    for student in Student.students:
        student.display()

if __name__ == "__main__":
    main()