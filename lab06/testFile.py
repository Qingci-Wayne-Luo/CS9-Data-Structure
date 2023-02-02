# testFile.py

from Apartment import Apartment
from lab06 import mergesort, ensureSortedAscending, getBestApartment, getWorstApartment, getAffordableApartments

def test_Apartment():
    a0 = Apartment(1204, 200, "bad")
    assert a0.getRent() == 1204
    assert a0.getMetersFromUCSB() == 200
    assert a0.getCondition() == 'bad'
    assert a0.getApartmentDetails() == \
           "(Apartment) Rent: $1204, Distance From UCSB: 200m, Condition: bad"

def test_Overload():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1000, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    assert a5.__lt__(a0) == True
    assert a1.__lt__(a2) == False
    assert a3.__lt__(a2) == False
    assert a5.__lt__(a4) == False

def test_apartmentList1():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(950, 215, "average")
    a2 = Apartment(950, 215, "excellent")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert ensureSortedAscending(apartmentList) == True
    assert apartmentList[2].getApartmentDetails() == \
            '(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent'
    assert apartmentList[4].getApartmentDetails() == \
           '(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average'
           
def test_apartmentList2():
    a0 = Apartment(1200, 200, "average")
    a1 = Apartment(1200, 200, "excellent")
    a2 = Apartment(1000, 100, "average")
    a3 = Apartment(1000, 215, "excellent")
    a4 = Apartment(700, 315, "bad")
    a5 = Apartment(800, 250, "excellent")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    assert ensureSortedAscending(apartmentList) == False
    mergesort(apartmentList)
    assert getBestApartment(apartmentList) == \
           '(Apartment) Rent: $700, Distance From UCSB: 315m, Condition: bad'
    assert getWorstApartment(apartmentList) == \
           '(Apartment) Rent: $1200, Distance From UCSB: 200m, Condition: average'

def test_apartmentList3():
    a0 = Apartment(1115, 215, "bad")
    a1 = Apartment(970, 215, "average")
    a2 = Apartment(950, 215, "average")
    a3 = Apartment(950, 190, "excellent")
    a4 = Apartment(900, 190, "excellent")
    a5 = Apartment(500, 250, "bad")
    apartmentList = [a0, a1, a2, a3, a4, a5]
    mergesort(apartmentList)
    assert getAffordableApartments(apartmentList, 950) == \
            '(Apartment) Rent: $500, Distance From UCSB: 250m, Condition: bad'+'\n'+\
            '(Apartment) Rent: $900, Distance From UCSB: 190m, Condition: excellent'+'\n'+\
            '(Apartment) Rent: $950, Distance From UCSB: 190m, Condition: excellent'+'\n'+\
            '(Apartment) Rent: $950, Distance From UCSB: 215m, Condition: average'           
    












    
                                               
                                               
    
    
