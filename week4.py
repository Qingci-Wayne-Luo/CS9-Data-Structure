# WEEK4

'''Recursion/ how many python manage recursion in memeory/ analyzing it
* when a function contains a call to itself
* recursive solution are useful when the result is dependent on the result
of SUB-PARTS of the problem

The three laws of recursion
1. A recursive algo must have a BASE case
2. A recursive algo must change its state and move toward the BASE case
3. A recursive algo must call itself, recursively
'''

'''
Factorial:

N! = N * (N-1) * (N-2) * ... * 2 * 1

N! = N * (N-1)!

0! == 1
'''

def factorial(n): # n is a positive integer
    # base case
    if n == 0:
        return 1
    return n * factorial(n-1)

assert factorial(0)==1
assert factorial(2)==2
assert factorial(4)==24


def double(n):
    return 2 * n

def triple(n):
    return n + double(n)


# Example: Fibonacci
# f(n) = f(n-1) + f(n-2)
# f(0) = 0, f(1) = 1, f(2) = 1, f(3) = 2, f(4) = 3, f(5) = 5
# f(6) = 8

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
    










    
