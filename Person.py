class Person:
    name = ""
    age = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"My name is {self.name} and my age is {self.age}")