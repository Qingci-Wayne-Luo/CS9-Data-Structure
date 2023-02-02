# testFile.py

from Book import Book
from BookCollectionNode import BookCollectionNode
from BookCollection import BookCollection

def test_Book():
    b0 = Book("Cujo", "King, Stephen", 1981)
    assert b0.getTitle() == "Cujo"
    assert b0.getAuthor() == "King, Stephen"
    assert b0.getYear() == 1981
    assert b0.getBookDetails() == "Title: Cujo, Author: King, Stephen, Year: 1981"

def test_BookCollectionNode():
    b0 = Book("Cujo", "King, Stephen", 1981)
    n = BookCollectionNode(b0)
    assert n.getData() == b0
    assert n.getNext() == None
    

def test_SetData():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    n = BookCollectionNode(b0)
    n.setData(b1)
    assert n.getData() == b1

def set_NodesetNext():
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("Ready Player One", "Cline, Ernest", 2011) 
    n = BookCollectionNode(b0)
    n1 = BookCollectionNode(b1)
    n.setNext(n1)
    assert n.getNext() == n1

def test_BookCollection():
    bc = BookCollection()
    assert bc.getNumberOfBooks() == 0
    b0 = Book("Cujo", "King, Stephen", 1981)
    b1 = Book("The Shining", "King, Stephen", 1977)
    b2 = Book("Ready Player One", "Cline, Ernest", 2011)
    b3 = Book("Rage", "King, Stephen", 1977)
    bc.insertBook(b0)
    bc.insertBook(b1)
    bc.insertBook(b2)
    bc.insertBook(b3)
    assert bc.getNumberOfBooks() == 4
    assert print(bc.getBooksByAuthor("Cline, Ernest"))== \
    print("Title: Ready Player One, Author: Cline, Ernest, Year: 2011")
    assert print(bc.getBooksByAuthor("KING, Stephen"))== \
    print("Title: Rage, Author: King, Stephen, Year: 1977" + "\n"
    "Title: The Shining, Author: King, Stephen, Year: 1977" + "\n" 
    "Title: Cujo, Author: King, Stephen, Year: 1981")
    assert print(bc.getAllBooksInCollection()) == \
    print("Title: Ready Player One, Author: Cline, Ernest, Year: 2011" + "\n" \
    "Title: Rage, Author: King, Stephen, Year: 1977" + "\n" \
    "Title: The Shining, Author: King, Stephen, Year: 1977" + "\n" \
    "Title: Cujo, Author: King, Stephen, Year: 1981")
    assert print(bc.removeAuthor("King, Stephen")) == \
    print ("Title: Ready Player One, Author: Cline, Ernest, Year: 2011")
    assert print(bc.removeAuthor("Cline, Ernest")) ==\
    print("Title: Rage, Author: King, Stephen, Year: 1977" + "\n"
    "Title: The Shining, Author: King, Stephen, Year: 1977" + "\n" 
    "Title: Cujo, Author: King, Stephen, Year: 1981")
   









    

    
