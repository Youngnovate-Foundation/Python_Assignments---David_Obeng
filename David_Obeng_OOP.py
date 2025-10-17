class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.__grade = grade

    # Getter method
    def get_grade(self):
        return self.__grade
    
    # Setter method
    def set_grade(self, grade):
        self.__grade = grade

    def display_info(self):
        return f'Name: {self.name}, age: {self.age} and Grade: {self.__grade}.'

# Gruaduate Student Class
class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        super().__init__(name, age, grade)
        self.degree = degree

    # Overiding display Info method.
    def display_info(self):
        return f'Graduate Student - Name: {self.name}, Age: {self.age}, Grade: {self._Student__grade} and Degree: {self.degree}.'
    

# Objects 
std1 = Student("Kwame Ansah", 21, "C")
std2 = Student("Sarah Odom", 25, "D")
std3 = Student("Samuel Sam", 24, "B")
grad1 = GraduateStudent("David Obeng", 23, "A", "Doctor of Science")
grad2 = GraduateStudent("Amy Oteng", 24, "C", "Bachelor of Arts")

# Displaying Info
print(std1.display_info())
print(grad1.display_info())

#Getter and Setter Methods
print(std2.get_grade())
std2.set_grade("A")
print(std2.get_grade())

# Polymorphysm
students = [std1, std2, std3, grad1, grad2]

for student in students:
    print(student.display_info())
