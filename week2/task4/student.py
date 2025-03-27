from person import Person


class Student(Person):
    def __init__(self, name, age, email, student_id, grades):
        super().__init__(name, age, email)
        self.student_id = student_id
        self.grades = grades

    def add_grade(self, course, grade):
        self.grades[course] = grade

    def display_info(self):
        return super().display_info() + f"\nStudent ID: {self.student_id}\nGrades: {self.grades}"

    def __str__(self):
        return self.display_info()