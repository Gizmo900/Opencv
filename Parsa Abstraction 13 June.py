from abc import ABC, abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class circle(shape):
    def __init__(self, radius):
        self.radius = radius


    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    def description(self):
        return "This is a circle with radius " + str(self.radius)
        

c1 = circle(5)
print("Area of the circle:", c1.area())
print("Perimeter of the circle:", c1.perimeter())
print("Description of the circle:", c1.description())
