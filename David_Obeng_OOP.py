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
        if 1.0 < grade < 5.0:
            self.__grade = grade
        else:
            print('Grade must be between 1.0 and 5.0 \n')

    def display_info(self):
        return f'Name: {self.name} \nAge: {self.age} \nGrade: {self.__grade}'

# Gruaduate Student Class
class GraduateStudent(Student):
    def __init__(self, name, age, grade, degree):
        super().__init__(name, age, grade)
        self.degree = degree

    # Overiding display Info method.
    def display_info(self):
        return f'Name: {self.name} \nAge: {self.age} \nGrade: {self._Student__grade} \nDegree: {self.degree}.'
    

# Objects 
std1 = Student("Kwame Ansah", 21, 1)
std2 = Student("Sarah Odom", 25, 4)
std3 = Student("Samuel Sam", 24, 1)
grad1 = GraduateStudent("David Obeng", 23, 2, "Doctor of Science")
grad2 = GraduateStudent("Amy Oteng", 24, 4.5, "Bachelor of Arts")

# Displaying Info
print('_________Student 1__________')
print(std1.display_info() + '\n')
print('_________Student 2__________')
print(std2.display_info()  + '\n')
print('_________Student 3__________')
print(std3.display_info()  + '\n')
print('______Grad. Student 1_______')
print(grad1.display_info()  + '\n')
print('______Grad. Student 2_______')
print(grad2.display_info()  + '\n')

#Getter and Setter Methods
print(std2.get_grade())
std2.set_grade(2)
print(std2.get_grade())
print('\n')

# Setting Grade greater than 5
std3.set_grade(6)

# Polymorphysm
students = [std1, std2, std3, grad1, grad2]

for student in students:
    print('========================')
    print(student.display_info())
    print('======================== \n')
