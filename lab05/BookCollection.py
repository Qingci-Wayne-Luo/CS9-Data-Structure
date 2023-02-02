# BookCollection.py

from Book import Book
from BookCollectionNode import BookCollectionNode

class BookCollection(BookCollectionNode):
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getNumberOfBooks(self):
        #the same method as length method in lecture 10
        temp = self.head
        count = 0
        while temp != None:
            count += 1
            temp = temp.getNext()
        return count

    def insertBook(self, book):
        # very similar to the add method in lecture 11
        # except using overload operator gt on this one
        current = self.head
        previous = None
        stop = False

        while current != None and not stop:
            if current.getData().__gt__(book):
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = BookCollectionNode(book)
            # insert at the front of the list
        if previous == None:
            temp.setNext(self.head)
            self.head = temp
        else: # insert not at front of list
            temp.setNext(current)
            previous.setNext(temp)

    def getBooksByAuthor(self, author):
        # very similar to the getList method in lecture 11
        current = self.head
        output = ''
        while current != None:
            if author.lower() == current.getData().getAuthor().lower():
                output += str (current.getData().getBookDetails())+ "\n"
                current = current.getNext()
            else:
                current = current.getNext()
        return output

    def getAllBooksInCollection(self):
        current = self.head
        output = ''
        while current != None:
            output+=str(current.getData().getBookDetails())+'\n'
            current = current.getNext()
        return output
        
    def removeAuthor(self, author):
        current = self.head
        if current == None:
            return

        previous = None
        found = False
        while not found:
            if current == None:
                return
            if author.lower() == current.getData().getAuthor().lower():
                found = True
            else:
                previous = current
                current = current.getNext()

        #remove 1st author
        if found == True and previous == None:
            self.head = current.getNext()

        #remove not 1st author
        if found == True and previous != None:
            previous.setNext(current.getNext())























        







        
