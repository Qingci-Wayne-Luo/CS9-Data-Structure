# testFile.py

from Pizza import Pizza
from CustomPizza import CustomPizza
from SpecialtyPizza import SpecialtyPizza
from PizzaOrder import PizzaOrder
from OrderQueue import OrderQueue

def test_getSize():
    cp0 = CustomPizza("M")
    assert cp0.getSize() == "M"

def test_getPrice():
    cp0 = CustomPizza("L")
    assert cp0.getPrice() == 12.00

def test_setSize():
    cp0 = CustomPizza("M")
    cp0.setSize("L")
    assert cp0.getSize() == "L"

def test_addTopping():
    cp1 = CustomPizza("M")
    cp1.addTopping("extra cheese")
    assert cp1.getPrice() == 10.75
    cp1 = CustomPizza("S")
    cp1.addTopping("bacon")
    cp1.addTopping("sausage")
    assert cp1.getPrice() == 9.00

def test_getPizzaDetails():
    cp1 = CustomPizza("S")

    assert cp1.getPizzaDetails() == \
       "CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n"

    cp1 = CustomPizza("L")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")

    assert cp1.getPizzaDetails() == \
        "CUSTOM PIZZA\n\
Size: L\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $14.00\n"

    sp1 = SpecialtyPizza("S", "Carne-more")
    assert sp1.getPizzaDetails() == \
           "SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"

    sp2 = SpecialtyPizza("L", "Texas BBQ")
    assert sp2.getPizzaDetails() == \
           "SPECIALTY PIZZA\n\
Size: L\n\
Name: Texas BBQ\n\
Price: $16.00\n"

def test_addPizza():
    cp1 = CustomPizza("S")
    order = PizzaOrder(92532)
    order.addPizza(cp1)
    assert order.getOrderDescription() == \
           "******\n\
Order Time: 92532\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
Price: $8.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $8.00\n\
******\n"

def test_getOrderDescription():
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    sp1 = SpecialtyPizza("S", "Carne-more")
    order = PizzaOrder(123000)  # 12:30:00PM
    order.addPizza(cp1)
    order.addPizza(sp1)

    assert order.getOrderDescription() == \
           "******\n\
Order Time: 123000\n\
CUSTOM PIZZA\n\
Size: S\n\
Toppings:\n\
\t+ extra cheese\n\
\t+ sausage\n\
Price: $9.00\n\
\n\
----\n\
SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n\
\n\
----\n\
TOTAL ORDER PRICE: $21.00\n\
******\n"


def test_OrderQueue():
    oq = OrderQueue()
    cp1 = CustomPizza("S")
    cp1.addTopping("extra cheese")
    cp1.addTopping("sausage")
    order1 = PizzaOrder(123000)
    order1.addPizza(cp1)

    sp1 = SpecialtyPizza("M", "Woodstock Pizza")
    order2 = PizzaOrder(131423)
    order2.addPizza(sp1)

    sp2 = SpecialtyPizza("L", "Texas BBQ")
    order3 = PizzaOrder(92532)
    order3.addPizza(sp2)

    oq.addOrder(order1)
    oq.addOrder(order2)
    oq.addOrder(order3)

    assert oq.processNextOrder() == order3.getOrderDescription()
    assert oq.processNextOrder() == order1.getOrderDescription()
    assert oq.processNextOrder() == order2.getOrderDescription()
