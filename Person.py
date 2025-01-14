class Person:
    name = ""
    age = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Person name is {self.name} `and age is {self.age}`")