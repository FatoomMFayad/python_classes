from Person import Person


class Student(Person):
    section=""

    def __init__(self, name, age, section):
        super.__init__(name, age)
        self.section = section
    