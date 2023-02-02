from Animal import Animal


class AnimalShelter:
    def __init__(self):
        self.shelter = {}

    def addAnimal(self, animal):
        if self.shelter.get(animal.species) == None:
            self.shelter[animal.species] = [animal]
        elif not animal in self.shelter.get(animal.species):
            self.shelter[animal.species].append(animal)
            
    def removeAnimal(self, animal):
        if animal.species in self.shelter:
            for i in self.shelter[animal.species]:
                if (i.species == animal.species) and (i.weight == animal.weight) \
                    and (i.age == animal.age) and (i.name == animal.name):
                    self.shelter[animal.species].remove(animal)
    
    def removeSpecies(self, species):
        if species != None:
            species = species.upper()
        if species in self.shelter.keys():
            del self.shelter[species]
    
    def getAnimalsBySpecies(self, species):
        
        if species != None: 
            species = species.upper()
        
        if species in self.shelter:
            if len(self.shelter[species]) > 0:
                return "\n".join([i.toString() for i in self.shelter[species]])
        return ""

    def doesAnimalExist(self, animal):
        if animal.species in self.shelter:
            if animal in self.shelter[animal.species]:
                return True
            else: return False
        else: return False
