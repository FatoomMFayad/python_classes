class Rectangle:
    width = 0
    length = 0

    def perimeter(self):
       return (self.length + self.width) * 2

    def area(self):
        return (self.length * self.width)

    def display(self):
        return print(f"Rectangle:\nwidth = {self.width},\nlength = {self.length}, \nperimeter = {self.perimeter()},\narea = {self.area()}")


r1 = Rectangle()
r1.width = 10
r1.length = 20
r1.perimeter()
r1.area()
r1.display()

