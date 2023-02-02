#lab03.py

def integerDivision(n,k):
    if n == 0:
        return 0
    if n < k:
        return 0
    return 1 + integerDivision(n-k,k)


def collectEvenInts(listOfInt):
    if len(listOfInt) == 0:
        return []
    else:
        for i in listOfInt:
            if i%2 == 0:
                return [listOfInt[0]] + collectEvenInts(listOfInt[1:])
            elif i%2 == 1:
                return collectEvenInts(listOfInt[1:])
            else:
                return []

def countVowels(someString):
    if len(someString) == 0:
        return 0
    else:
        if someString[0] in ['A','E','I','O','U','a','e','i','o','u']:
            return 1 + countVowels(someString[1:])
        elif someString[0] not in ['A','E','I','O','U','a','e','i','o','u']:
            return 0 + countVowels(someString[1:])
        else:
            return 0

def reverseString(s):
    if len(s) == 0:
        return ''
    return reverseString(s[1:]) + s[0]


def removeSubString(s,sub):
    if len(s) >= 1:
        if (s[0] + removeSubString(s[1:],sub))[:len(sub)] == sub:
            return (s[0] + removeSubString(s[1:],sub))[len(sub):]
        elif s[0] + removeSubString(s[1:],sub)[:len(sub)] != sub:
            return s[0] + removeSubString(s[1:],sub)
    else:
        return ''










