# CarInventory.py

from CarInventoryNode import CarInventoryNode
from Car import Car

class CarInventory:
    def __init__(self):
        self.root = None

    def addCar(self, car):
        if self.root:
            self._put(CarInventoryNode(car),self.root)
        else:
            self.root = CarInventoryNode(car)


    def _put(self, tempNode, currentNode):
        if tempNode == currentNode:
            currentNode.cars.append(tempNode.cars[0])
        elif tempNode < currentNode:
            if currentNode.getLeft():
                self._put(tempNode, currentNode.left)
            else:
                currentNode.left = tempNode
                tempNode.parent = currentNode
                       
        else:
            if currentNode.getRight():
                self._put(tempNode, currentNode.right)
            else:
                currentNode.right = tempNode
                tempNode.parent = currentNode

               
    def doesCarExist(self, car):
        if self.root:
            res = self._get(CarInventoryNode(car), self.root)
            #If we get a node from the helper,
            #we can iterate through the cars list and check
            if res:
                for i in res.cars:
                    if i == car:
                        return True
            else:
                return False
        else:
            return False


    def getBestCar(self, make, model):
        '''We can always create a temporary Car object,
        where we give it the make and model from the
        parameter, but some arbitrary value for year and price
        '''
        TempCar = Car(make, model, 2022, 20000)
        TempNode = CarInventoryNode(TempCar)
        if self.root:
            res = self._get(TempNode, self.root)
            if res:
                #initialized max to first element
                maxVal = res.cars[0] 
                for i in range(0, len(res.cars),1):
                    maxVal = max(maxVal, res.cars[i])
                return maxVal
            else:
                return None
        else:
            return None

    def getWorstCar(self, make, model):
            
        TempCar = Car(make, model, 2022, 20000)
        TempNode = CarInventoryNode(TempCar)
        if self.root:
            res = self._get(TempNode, self.root)
            if res:
                minVal = res.cars[0] 
                for i in range(0, len(res.cars),1):
                    minVal = min(minVal, res.cars[i])
                return minVal
            else:
                return None
        else:
            return None


    def _get(self, Node, currentNode):
        if not currentNode:
            return None
        elif Node == currentNode:
            return currentNode
        elif Node < currentNode:
            return self._get(Node, currentNode.left)
        else:
            return self._get(Node, currentNode.right)

    def preOrder(self):
        ret = ""
        if self.root:
            ret = self.root.preOrder_helper()
        return ret

    def inOrder(self):
        ret = ""
        if self.root:
            ret = self.root.inOrder_helper()
        return ret

    def postOrder(self):
        ret = ""
        if self.root:
            ret = self.root.postOrder_helper()
        return ret

    def getTotalInventoryPrice(self):
        total = 0
        if self.root:
            total = self.root.getTotal_helper()
        return total
   
    





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







        


    
