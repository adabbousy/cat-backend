from person import Person


class Teacher(Person):
    def __init__(self, name, age, email, teacher_id, subject):
        super().__init__(name, age, email)
        self.teacher_id = teacher_id
        self.subject = subject

    def display_info(self):
        return super().display_info() + f"\nTeacher ID: {self.teacher_id}\nSubject: {self.subject}"

    def __str__(self):
        return self.display_info()
