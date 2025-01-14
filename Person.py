from traceback import print_tb


class Person:
    name = ""
    age = ""
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        return print(f"Person name is {self.name} `and age is {self.age}`")