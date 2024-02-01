from abc import abstractmethod


class Shape():
    @abstractmethod
    def area(self):
        pass
    
class Square(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius

circle = Circle(5)
square = Square(7)
print(circle.area())
print(square.area())