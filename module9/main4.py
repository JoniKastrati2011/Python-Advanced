import math

class Shape:
    def area(self):
        pass


def Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

        def area(self):
            return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height


class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return 0.5 * self.width * self.height
Circle = Circle(5)
rectangle = Rectangle(10, 6)
Triangle = Triangle(5, 6)

print("Area of the circle is", circle.area)
print("Area of the circle is", rectangle.area)
print("Area of the circle is", triangle.area)
