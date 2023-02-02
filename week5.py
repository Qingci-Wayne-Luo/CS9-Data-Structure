# LindkedList.py

'''Linked Lists
* Python lists are just one way to implement a List type structure
* The underlying structure of a Python List uses the concept of storing
information in CONTIGUOUS memory
* There is a another way to implement a List type structure that performs
better in certain operations (and worse in others)
    *This doesn't organize data in contiguous memory, so maintaining the list
    structure doesn't need to shift elements around
*LINKED LISTS is a list structure that is not stored in contiguous memory
    * BUT this structure still provides relative positioning of the data
    in the list

Linked Lists
* Object that MANAGES and MAINTAINS the chain of nodes as a collection
* Contain a head reference to the first node in the Linked List
    * As long as we know where the first element is , we can "walk" down
    the linked list and visit every node structure
    * Methods in the LinkedList class should maintain the links between
    the nodes

'''

'''def bubbleSort(aList):
    for passnum in range(len(aList)-1,0,-1):
        for i in range(passnum):
            if aList[i] > aList[i+1]:
                # swap (bubble up!)
                temp = aList[i]
                aList[i] = aList[i+1]
                aList[i+1] = temp
            print(aList,passnum,i)

print(bubbleSort([7,5,6,2,1]))
'''

'''def selectionSort(aList):
	for fillslot in range(len(aList)-1,0,-1):
		positionOfMax=0
		for location in range(1,fillslot+1):
			if aList[location]>aList[positionOfMax]:
				positionOfMax = location
			print(aList, fillslot)

		# swap largest element in correct place
		temp = aList[fillslot]
		aList[fillslot] = aList[positionOfMax]
		aList[positionOfMax] = temp
    
print(selectionSort([4,8,3,5,7]))
'''

def insertionSort(aList):
	for index in range(1,len(aList)):

		currentvalue = aList[index]
		position = index

		# shift elements over by one
		while position > 0 and aList[position-1] > currentvalue:
			aList[position] = aList[position-1]
			position = position-1
		

		# insert element in appropriate place
		aList[position] = currentvalue
		print(aList, index)

print(insertionSort([8,4,5,3,7]))




'''  
class Node:
    def __init__(self, data):
		self.data = data
		self.next = None

    def getData(self):
		return self.data

    def getNext(self):
		return self.next

    def setData(self, newData):
		self.data = newData

    def setNext(self, newNext):
		self.next = newNext

class LinkedList:
    def __init__(self):
		self.head = None

    def isEmpty(self):
		return self.head == None

    def addToFront(self, item):
		temp = Node(item)
		temp.setNext(self.head)
		self.head = temp

    def length(self):
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext() # taking a step down the list
        return count

    def search(self, item):
        temp = self.head
        found = False
        while temp != None and not found:
            if temp.getData() == item:
                found = True
            else:
                temp = temp.getNext()

        return found


'''








		



		
