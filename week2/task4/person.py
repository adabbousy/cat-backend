class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def display_info(self):
        return f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}"

    def __str__(self):
        return self.display_info()
