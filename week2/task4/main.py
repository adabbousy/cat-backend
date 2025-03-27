from student import Student
from teacher import Teacher
from course import Course
from gradebook import Gradebook

gradebook = Gradebook()

s1 = Student("Alice", 18, "alice@gmail.com", 85497, {"Math": 90, "Art": 95})
s2 = Student("Bob", 19, "bob@gmail.com", 59652, {"Math": 80, "Art": 91})
t1 = Teacher("John", 40, "john@gmail.com", 100, "Math")

gradebook.add_student(s1)
gradebook.add_student(s2)

c1 = Course("Math", t1)
c1.enroll(s1)
c1.enroll(s2)

print(gradebook)

s3 = Student("Charlie", 20, "charlie@gmail.com", 10291, {})
gradebook.add_student(s3)

c2 = Course("Science", t1)

print(gradebook)
