# Super = Function used in a child class to call methods from a parent class.
# Allows to extend functionality of the inherited methods.

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"It is {self.color} and {'filled' if self.filled else 'Not Filled'}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"It if a circle of area {3.14 * self.radius * self.radius} cm2")
        
    
class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width
    
    def describe(self):
        print(f"It is a circle with an area of {self.width * self.width} cm2")
        super().describe()

class Rectangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        print(f"It is a rectangle with area {self.width * self.height}cm2")
        super().describe()

circle = Circle("Red", False, 5)
square = Square("Blue", False, width=6)
rectangle = Rectangle("Green", True, 7, 8)
print(circle.color)

print(circle.radius)

print(circle.filled)
circle.describe()


print(square.color)

print(square.filled)

print(square.width)
square.describe()

print(rectangle.color)

print(rectangle.filled)
print(rectangle.width)


print(rectangle.height)
rectangle.describe()

