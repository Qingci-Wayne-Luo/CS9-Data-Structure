#testFile.py

from Car import Car
from CarInventoryNode import CarInventoryNode
from CarInventory import CarInventory

def test_Car():

    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    assert car1.make == 'DODGE'
    assert car1.model == 'DART'
    assert car1.year == 2015
    assert car1.price != 5000
    assert (car1 > car2)
    assert not (car1 < car2)
    assert not (car1 == car2)

def test_CarInventoryNode():
    car1 = Car("Dodge", "dart", 2015, 6000)
    car2 = Car("dodge", "DaRt", 2003, 5000)
    car3 = Car("Honda", "CRV", 2007, 8000)

    assert car1.year == 2015
    assert car3.price == 8000
    assert (car1 < car3)
    assert (car2 < car3)
    assert not car1 == car3
    assert car3.__str__() == \
           "Make: HONDA, Model: CRV, Year: 2007, Price: $8000"

    carNode = CarInventoryNode(car1)
    carNode.cars.append(car2)
    carNode.cars.append(car3)
    assert carNode.__str__() == \
"""\
Make: DODGE, Model: DART, Year: 2015, Price: $6000\n\
Make: DODGE, Model: DART, Year: 2003, Price: $5000\n\
Make: HONDA, Model: CRV, Year: 2007, Price: $8000\n\
"""



            
def test_CarInventory():
    bst = CarInventory()

    car1 = Car("Nissan", "Leaf", 2018, 18000)
    car2 = Car("Tesla", "Model3", 2018, 50000)
    car3 = Car("Mercedes", "Sprinter", 2022, 40000)
    car4 = Car("Mercedes", "Sprinter", 2014, 25000)
    car5 = Car("Ford", "Ranger", 2021, 25000)

    bst.addCar(car1)
    bst.addCar(car2)
    bst.addCar(car3)
    bst.addCar(car4)
    bst.addCar(car5)

    assert bst.root == CarInventoryNode(car1)
    assert bst.root.__str__() == \
           "Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000\n"

    assert bst.root.right == CarInventoryNode(car2)
    assert bst.root.right.__str__() == \
           "Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000\n"
    assert bst.root.left == CarInventoryNode(car3)
    assert bst.root.left.__str__() == \
           "Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n"
    assert bst.root.left == CarInventoryNode(car4)
    assert bst.root.left.__str__() == \
           "Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000\n\
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000\n"

    assert bst.root.left.left == CarInventoryNode(car5)
    assert bst.root.left.left.__str__() == \
           "Make: FORD, Model: RANGER, Year: 2021, Price: $25000\n"

        
    assert bst.doesCarExist(car1)
    assert bst.doesCarExist(car2)
    assert bst.doesCarExist(car3)
    assert bst.doesCarExist(car4)
    assert bst.doesCarExist(car5)

    assert bst.getBestCar("Nissan", "Leaf") == car1
    assert bst.getBestCar("Mercedes", "Sprinter") == car3
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getWorstCar("Nissan", "Leaf") == car1
    assert bst.getWorstCar("Mercedes", "Sprinter") == car4
    assert bst.getBestCar("Honda", "Accord") == None

    assert bst.getTotalInventoryPrice() == 158000
    
    assert bst.inOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.preOrder() == \
"""\
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
"""
    assert bst.postOrder() == \
"""\
Make: FORD, Model: RANGER, Year: 2021, Price: $25000
Make: MERCEDES, Model: SPRINTER, Year: 2022, Price: $40000
Make: MERCEDES, Model: SPRINTER, Year: 2014, Price: $25000
Make: TESLA, Model: MODEL3, Year: 2018, Price: $50000
Make: NISSAN, Model: LEAF, Year: 2018, Price: $18000
"""







    
