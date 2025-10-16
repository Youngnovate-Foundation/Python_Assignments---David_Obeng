class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.__grade = grade

    def display_info(self):
        print(f'Name: {self.name}, age: {self.age} and Grade: {self.grade}.')

class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        super().__init__(name, age, grade)
        self.degree = degree

    