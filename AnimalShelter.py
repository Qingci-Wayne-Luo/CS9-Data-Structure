#Wayne Luo
#AnimalShelter.py

from Animal import Animal

class AnimalShelter:

    def __init__(self):
        self.AnimalShelter = {}

    def addAnimal(self, animal):
        if self.AnimalShelter.get(animal.species) == None:
            self.AnimalShelter[animal.species] = [animal]

        elif not animal.species in self.AnimalShelter.get(animal.species):
            self.AnimalShelter[animal.species].append(animal)

    def removeAnimal(self, animal):
        if animal.species in self.AnimalShelter:
            for element in self.AnimalShelter[animal.species]:
                if element.name == animal.name and element.age == animal.age and element.weight == animal.weight:
                    self.AnimalShelter[animal.species].remove(animal)

    def removeSpecies(self, species):
        if species in self.AnimalShelter:
            self.AnimalShelter.pop(species)

    def getAnimalsBySpecies(self, species):
        string = ""
        if species in self.AnimalShelter:
            for i in range(len(self.AnimalShelter[species])):
                string = string + self.AnimalShelter[species][i].toString() + '\n'
        return string
        

    def doesAnimalExist(self, animal):
        if animal.species in self.AnimalShelter:
            if animal in self.AnimalShelter[animal.species]:
                return True
            else:
                return False
        else: return False
            




















        
