#testFile.py

from lab03 import integerDivision
from lab03 import collectEvenInts
from lab03 import countVowels
from lab03 import reverseString
from lab03 import removeSubString

def test_integerDivision():
    assert integerDivision(27,4) == 6
    assert integerDivision(3,5) == 0
    assert integerDivision(0,2) == 0
    assert integerDivision(3,3) == 1
    assert integerDivision(6,3) == 2

def test_collectEvenInts():
    assert collectEvenInts([1,2,3,4,5]) == [2,4]
    assert collectEvenInts([1]) == []
    assert collectEvenInts([]) == []
    assert collectEvenInts([1,3,5,7,9,11]) == []
    assert collectEvenInts([2,4,6,8,10]) == [2,4,6,8,10]

def test_countVow():
    assert countVowels("Wayne is cool") == 5
    assert countVowels("This Is A String") == 4
    assert countVowels("") == 0
    assert countVowels("glyph") == 0

def test_reverseString():
    assert reverseString('CMPSC9') == '9CSPMC'
    assert reverseString('Wayne') == 'enyaW'
    assert reverseString('') == ''
    assert reverseString('WolloW') == 'WolloW'

def test_removeSubString():
    assert removeSubString('Lolololol','lol') == 'Loo'
    assert removeSubString('Wa','Wayne') == 'Wa'
    assert removeSubString('Wowowowow','wow') == 'Woo'
    assert removeSubString('','co') == ''
    assert removeSubString('Cool','') == 'Cool'
    
