class Gradebook:
    def __init__(self):
        self.gradebook = {}

    def add_student(self, student):
        if student.name not in self.gradebook:
            self.gradebook[student.name] = {"age": student.age, "email": student.email}
        for course, grade in student.grades.items():
            self.gradebook[student.name][course] = grade

    def display_info(self):
        for name, info in self.gradebook.items():
            print(f"Name: {name}")
            for key, value in info.items():
                if key != name:
                    print(f"\t{key}: {value}")
            print()

    def __str__(self):
        result = []
        for name, info in self.gradebook.items():
            student_info = [f"Name: {name}"]
            for key, value in info.items():
                student_info.append(f"\t{key}: {value}")
            result.append("\n".join(student_info))
        return "\n\n".join(result)
