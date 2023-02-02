#Wayne Luo
#Animal.py

class Animal:

    def __init__(self, species = None, weight = None, age = None, name = None):
        self.species = species
        self.weight = weight
        self.age = age
        self.name = name
        if not self.species:
            self.species = None
        else:
            self.species = species.upper()

        if not self.name:
            self.name = None
        else:
            self.name = name.upper()

    # Setter Method

    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = float(weight)

    def setAge(self, age):
        self.age = int(age)

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        return "Species: {}, Name: {}, Age: {}, Weight:{}" .format(self.species, self.name, self.age, self.weight)

a = Animal("dog", 12.2, 2, "Ruffles")
a.toString()
