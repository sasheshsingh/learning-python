# Polymophism: Greek Word: Poly - Many & Morphe - Form

# Two ways to achieve polymorphism:
# 1. Inheritance = An Object could be treated as same type as a parent class.
# 2. Duck Typing = Object must have necessary attributes/methods.
from abc import ABC, abstractmethod
class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius **2

class Square(Shape):
    def __init__(self, side):
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__()
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5

class Pizza(Circle):
    def __init__(self, radius, topping):
        super().__init__(radius)
        self.topping = topping

shapes = [Circle(5), Square(6), Triangle(3,4), Pizza(7, "Cheese")]

for shape in shapes:
    print(f"{shape.area()} cm2")