students = {}


def main():
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

        # Add student to students dictionary.
        add_student(name, subject, grade)

    # Print students records
    view_students()


def add_student(student, subject, grade):
    if student in students:
        # Append grades to list of grades if student found.
        students[student].append((subject, grade))
    else:
        # Add grades as a list if student not found.
        students[student] = [(subject, grade)]


def view_students():
    print("\nStudent Records:")
    # Loop over students and their list of grades.
    for student, records in students.items():
        print("\n".join([f"{student} -> {subject}: {grade}" for subject, grade in records]))


if __name__ == "__main__":
    main()