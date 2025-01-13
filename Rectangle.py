class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def Perimeter(self):
        return 2 * (self.length + self.width)

    def Area(self):
        return self.length * self.width

    def display(self):
        print(f"Length: {self.length}")
        print(f"Width: {self.width}")
        print(f"Perimeter: {self.Perimeter()}")
        print(f"Area: {self.Area()}")


r1 = Rectangle(10, 20)

r1.Perimeter()
r1.Perimeter()
r1.display()

