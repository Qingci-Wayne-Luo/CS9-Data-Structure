# lab06.py

from Apartment import Apartment

def mergesort(apartmentList):
	if len(apartmentList) > 1:
		mid = len(apartmentList) // 2

		# uses additional space to create the left / right
		# halves
		lefthalf = apartmentList[:mid]
		righthalf = apartmentList[mid:]

		# recursively sort the lefthalf, then righthalf
		mergesort(lefthalf)
		mergesort(righthalf)

		# merge two sorted sublists (left / right halves)
		# into the original list (alist)
		i = 0 # index for lefthalf sublist
		j = 0 # index for righthalf sublist
		k = 0 # index for alist

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] <= righthalf[j]:
				apartmentList[k] = lefthalf[i]
				i = i + 1
			else:
				apartmentList[k] = righthalf[j]
				j = j + 1
			k = k + 1

		# put the remaining lefthalf elements (if any) into
		# alist
		while i < len(lefthalf):
			apartmentList[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		# put the remaining righthalf elements (if any) into
		# alist
		while j < len(righthalf):
			apartmentList[k] = righthalf[j]
			j = j + 1
			k = k + 1

def ensureSortedAscending(apartmentList):
    index = 0
    while index < (len(apartmentList) - 1):
        if apartmentList[index] > apartmentList[index + 1]:
            return False
        index += 1
    return True

def getBestApartment(apartmentList):

    if len(apartmentList) > 1:
        mergesort(apartmentList)
        best = apartmentList[0].getApartmentDetails()
        return best

def getWorstApartment(apartmentList):

    if len(apartmentList) > 1:
        mergesort(apartmentList)
        worst = apartmentList[-1].getApartmentDetails()
        return worst

def getAffordableApartments(apartmentList, budget):
    mergesort(apartmentList)
    x = ''
    for index in range(len(apartmentList)):
        if apartmentList[index].getRent() <= budget:
            x += apartmentList[index].getApartmentDetails()+ "\n"
    x = x[:len(x)-1]
    return x
    
            
            
    
a0 = Apartment(1200, 200, "average")
a1 = Apartment(1200, 200, "excellent")
a2 = Apartment(1000, 100, "average")
a3 = Apartment(1000, 215, "excellent")
a4 = Apartment(700, 315, "bad")
a5 = Apartment(800, 250, "excellent")
apartmentList = [a0, a1, a2, a3, a4, a5]
        














            
