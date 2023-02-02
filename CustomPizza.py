# CustomPizza.py

from Pizza import Pizza

class CustomPizza(Pizza):

    def __init__(self, size):
        Pizza.__init__(self, size)
        self.toppingList = []
        if self.size == 'S':
            self.price = 8.00
        elif self.size == 'M':
            self.price = 10.00
        elif self.size == 'L':
            self.price = 12.00

    def addTopping(self, topping):
        self.toppingList.append(topping)
        if self.size == 'S' and len(self.toppingList)!=0:
            self.price = 8.00 + (0.5*len(self.toppingList))
        elif self.size == 'M' and len(self.toppingList)!=0:
            self.price = 10.00 + (0.75*len(self.toppingList))
        elif self.size == 'L' and len(self.toppingList)!=0:
            self.price = 12.00 + (1.00*len(self.toppingList))


    def getPizzaDetails(self):
        x = 'CUSTOM PIZZA\nSize: {}\n'.format(self.size)
        x += 'Toppings:\n'
        for i in self.toppingList:
            x += '\t+ ' + i + '\n'
        x += 'Price: ${:.2f}\n'.format(self.price)
        return x
        
        
        
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
