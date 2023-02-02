#Circle.py
from Shape2D import Shape2D

class Circle(Shape2D):

    def __init__(self, color = None, radius = None):
        self.color = color
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, radius):
        self.radius = radius

    def computeArea(self):
        return self.radius ** 2 * 3.14159
        

    def computePerimeter(self):
        return self.radius*2*3.14159 

    def getShapeProperties(self):
        return "Shape: CIRCLE, Color: {}, Radius: {}, Area: {}, Perimeter: {}"\
               .format(self.color, self.radius, self.computeArea(), self.computePerimeter())
        

c1=Circle("blue",2.5)
