class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.__grade = grade

    # Getter method
    def get_grade(self):
        return self.__grade

    # Display Student info
    def display_info(self):
        return f'Name: {self.name}, age: {self.age} and Grade: {self.__grade}.'

# Gruaduate Student Class
class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        super().__init__(name, age, grade)
        self.degree = degree

    # Overiding display Info method.
    def display_info(self):
        return f'Graduate Student - Name: {self.name}, Age: {self.age}, Grade: {self.grade} and Degree: {self.degree}.'