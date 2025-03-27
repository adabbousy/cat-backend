import os

students = {}
FILE_NAME = "students.csv"


def main():
    load_from_file(FILE_NAME)
    # Check if any data were loaded.
    if students:
        print("Loaded student records from file.")
        view_students()
    else:
        print("No previous records found. Starting fresh.")

    print(f"Enter 'exit' to stop inputting students.")
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

        # Add student to dictionary.
        add_student(name, subject, grade)

    # Save updated data to file.
    save_to_file(FILE_NAME)


def add_student(student, subject, grade):
    """Adds a student's subject and grade to the dictionary."""
    if student in students:
        # Append grades to list of grades if student found.
        students[student].append((subject, grade))
    else:
        # Add grades as a list if student not found.
        students[student] = [(subject, grade)]


def save_to_file(file):
    """Saves student records to a file in CSV format."""
    with open(file, 'w') as f:
        for student, record in students.items():
            for subject, grade in record:
                f.write(f"{student},{subject},{grade}\n")
    print("Data saved to file.")


def load_from_file(file):
    """Loads student records from a file if it exists."""
    # Check if file exists.
    if not os.path.exists(file):
        return

    # Read and add data to the dictionary
    with open(file, 'r') as f:
        for line in f:
            student, subject, grade = line.strip().split(',')
            add_student(student, subject, int(grade))


def view_students():
    """Displays all student records."""
    print("\nStudent Records:")
    # Loop over students and their list of grades.
    for student, records in students.items():
        print("\n".join([f"{student} -> {subject}: {grade}" for subject, grade in records]))


if __name__ == "__main__":
    main()