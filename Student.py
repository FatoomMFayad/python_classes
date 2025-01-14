from Person import Person


class Student(Person):
    section=""

    def __init__(self, name, age, section):
        super().__init__(name, age)
        self.section = section

    def displayStudent(self):
        super().display()
        print(f",and my Section is {self.section}")

student = Student("John", "18", "CSE")
student.displayStudent()