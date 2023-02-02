#Lecture3.py

'''
* Quiz this Friday 4/8
'''


'''Python objects
* onject-oriented programming is a way for programmers to define
their own python types and create abstractions of things with
the programming language.

* each object may have a certain state that gets modified
throughout program execution.

* object oriented programming is a way for programs to use and manipulate
objects to solve problems and model real-world properties.

* Object oriented is NOT REQUIRED
* It is more of a way to organze, read, maintain, test, and debug software
in a manageable way.
'''

class Student:
    '''student class type that contain student values'''

    def __init__(self):
        self.name = None
        self.perm = None
    
    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print("student name {}, perm: {}" .format(self.name, self.perm))



s = Student()
s.setName("Chris Gaucho")
s.setPerm(1111111)
s.printAttributes()




class Student:
    '''student class type that contain student values'''

    def __init__(self, name, perm):
        self.name = name
        self.perm = perm
    
    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print("student name: {}, perm: {}" .format(self.name, self.perm))



s = Student("Chris Gaucho", 1111111)
#s.setName("Chris Gaucho")
#s.setPerm(1111111)
s.printAttributes()






class Student:
    '''student class type that contain student values'''

    def __init__(self, name = None, perm = None):
        self.name = name
        self.perm = perm
    
    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print("student name {}, perm: {}" .format(self.name, self.perm))



#s = Student("Chris Gaucho", 1111111)
s = Student("Chris Gaucho")
#s.setName("Chris Gaucho")
#s.setPerm(1111111)
s.printAttributes()





class Student:
    '''student class type that contain student values'''

    def __init__(self, name = None, perm = None):
        self.name = name
        self.perm = perm
    
    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print("student name: {}, perm: {}" .format(self.name, self.perm))



#s = Student("Chris Gaucho", 1111111)
s = Student(perm = 1234567)
#s.setName("Chris Gaucho")
#s.setPerm(1111111)
s.printAttributes()



class Student:
    '''student class type that contain student values'''

    def __init__(self, name = None, perm = None):
        self.name = name
        self.perm = perm
    
    def setName(self, name):
        self.name = name

    def setPerm(self, perm):
        self.perm = perm

    def printAttributes(self):
        print("student name: {}, perm: {}" .format(self.name, self.perm))

s1 = Student("Jane",1234567)
s2 = Student("Joe", 7654321)
s3 = Student("Jill", 5555555)

studentList=[s1, s2, s3]

for s in studentList:
    s.printAttributes()


#s = Student("Chris Gaucho", 1111111)
#s = Student("Chris Gaucho")
#s.setName("Chris Gaucho")
#s.setPerm(1111111)
#s.printAttributes()






class Student:
    '''student class type that contain student values'''

    def __init__(self, name = None, perm = None):
        self.name = name
        self.perm = perm

    #Setter Method
    def setName(self, name):
        self.name = name
    
    def setPerm(self, perm):
        self.perm = perm

    #Getter Method
    def getName(self):
        return self.name

    def printAttributes(self):
        print("student name: {}, perm: {}" .format(self.name, self.perm))


s1 = Student()
assert s1.name == None
assert s1.perm == None

s1 = Student("Richert", 1234567)
s2 = Student("Gaucho", 7654321)

assert s1.name == "Richert"
assert s1.perm == 1234567
assert s2.name == "Gaucho"
assert s2.perm == 7654321









            
















