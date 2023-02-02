#testFile.py

from Shape2D import Shape2D
from Circle import Circle
from Square import Square

'''
These two below are from Shape2D.py
'''
def test_Shape2D():
    s1 = Shape2D("Green")
    assert s1.getColor() == "Green"
    assert s1.getShapeProperties() == "Shape: N/A, Color: Green"

def test_Shape2D_new():
    s2 = Shape2D("Grey")
    assert s2.getColor() == "Grey"
    s2.setColor("Black")
    assert s2.getColor() == "Black"
    assert s2.getShapeProperties() == "Shape: N/A, Color: Black"
    
    
def test_Circle():
    c1 = Circle("Green", 5.0)
    assert c1.getColor() == "Green"
    assert c1.getRadius() == 5.0
    assert c1.computeArea() == 78.53975
    assert c1.computePerimeter() == 31.4159
    assert c1.getShapeProperties() == "Shape: CIRCLE, Color: Green, Radius: 5.0, Area: 78.53975, Perimeter: 31.4159"
    c1.setRadius(1)
    assert c1.getRadius()== 1
    assert c1.computeArea() == 3.14159
    assert c1.computePerimeter() == 6.28318
    assert c1.getShapeProperties() == "Shape: CIRCLE, Color: Green, Radius: 1, Area: 3.14159, Perimeter: 6.28318"

def test_Square():
    sq = Square("Yellow", 4.0)
    assert sq.getColor() == "Yellow"
    assert sq.getSide() == 4
    assert sq.computeArea() == 16.0
    assert sq.computePerimeter() == 16.0
    assert sq.getShapeProperties() == "Shape: SQUARE, Color: Yellow, Side: 4.0, Area: 16.0, Perimeter: 16.0"
    sq.setColor("Red")
    sq.setSide(88.99)
    assert sq.getColor() == "Red"
    assert sq.getSide() == 88.99
    assert sq.computeArea() == 7919.2201
    assert sq.computePerimeter() == 355.96
    assert sq.getShapeProperties() == "Shape: SQUARE, Color: Red, Side: 88.99, Area: 7919.2201, Perimeter: 355.96"
    
    









    
