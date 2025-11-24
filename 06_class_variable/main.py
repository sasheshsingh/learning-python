## Class Variable = Shared among all instance of a class.
# These are defined outside the constructor.
# Allows to share data amoung all objects created from that class.


class Student:
    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1


student1 = Student("Spongebob", 30)

print(student1.name)
print(student1.age)
print(student1.class_year)
print(student1.num_students)

student2 = Student("Patrick", 35)

print(student2.name)
print(student2.age)
print(student2.class_year)
print(student2.class_year)

print(Student.class_year)

student3 = Student("Squidward", 55)


student4 = Student("Sandy", 27)

print(f"My Graduating class of {Student.class_year} has {Student.num_students}.")

print(student1.name)
print(student2.name)
print(student3.name)
print(student4.name)