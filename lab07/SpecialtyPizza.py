# SpecialtyPizza.py

from Pizza import Pizza

class SpecialtyPizza(Pizza):
    def __init__(self, size, name=''):
        Pizza.__init__(self, size)
        self.name = name

        if self.size == 'S':
            self.price = 12.00
        elif self.size == 'M':
            self.price = 14.00
        elif self.size == 'L':
            self.price = 16.00

    def getPizzaDetails(self):
        return'SPECIALTY PIZZA\nSize: {}\nName: {}\nPrice: ${:.2f}\n'\
            .format(self.size, self.name, self.price)
        
sp1 = SpecialtyPizza("S", "Carne-more")
assert sp1.getPizzaDetails() == \
"SPECIALTY PIZZA\n\
Size: S\n\
Name: Carne-more\n\
Price: $12.00\n"
