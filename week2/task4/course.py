from student import Student


class Course:
    def __init__(self, course_name, teacher, students=[]):
        self.course_name = course_name
        self.teacher = teacher
        self.students = students

    def enroll(self, student):
        if isinstance(student, Student) and student not in self.students:
            self.students.append(student)

    def display_info(self):
        return f"Course name: {self.course_name}\nTeacher: {self.teacher}\nStudents: {self.students}"

    def __str__(self):
        return self.display_info()