from Rectangle import Rectangle


class Parallelepipede(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height

    def Volume(self):
        return self.Area() * self.height

    def display(self):
        super().display()
        print(f"Height: {self.height}")
        print(f"Volume: {self.Volume()}")

p = Parallelepipede(10, 5, 8)
p.display()