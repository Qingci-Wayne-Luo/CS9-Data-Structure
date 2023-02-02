# CarInventoryNode.py
from Car import Car

class CarInventoryNode:
    def __init__(self, car):
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.cars = [car]
        self.parent = None
        self.left = None
        self.right = None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right

    def __str__(self):
        output = ''
        for i in self.cars:
            output += i.__str__() + '\n'
        return output

    def _gt__(self, rhs):
        if self.make > rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model > rhs.model:
                return True
        else:
            return False

    def __eq__(self, rhs):
        if (self.make == rhs.make) and (self.model == rhs.model):
            return True
        else:
            return False

    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        elif self.make == rhs.make:
            if self.model < rhs.model:
                return True
        else:
            return False

    def preOrder_helper(self):
        ret = ""
        if self:
            ret += self.__str__()
            if self.left:
                ret += self.left.preOrder_helper()
            if self.right:
                ret += self.right.preOrder_helper()
        return ret


    def inOrder_helper(self):
        ret = ""
        if self:
            if self.left:
                ret += self.left.inOrder_helper()
            ret += self.__str__()
            if self.right:
                ret += self.right.inOrder_helper()
        return ret

    
    def postOrder_helper(self):
        ret = ""
        if self:
            if self.left:
                ret += self.left.postOrder_helper()
            if self.right:
                ret += self.right.postOrder_helper()
            ret += self.__str__()
        return ret
        

    def getTotal_helper(self):
        total = 0
        if self:
            if self.left:
                total += self.left.getTotal_helper()
            if self.right:
                total += self.right.getTotal_helper()
            for i in self.cars:
                total += i.price
        return total








    
    
    
