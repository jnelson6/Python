'''
Created on Jan 29, 2018

@author: Julia Nelson

I pledge my honor that I have abided by the Stevens Honor System.
'''
from cs115 import reduce, range

def mult(a, b):
    """Returns the product of a and b """
    return a * b
 
def factorial(n):
    """Returns the positive integer input 'n' as its factorial. If n is 0 
    returns 1"""
    if n == 0:
        return 1
    return reduce(mult, range(1, n+1))

def add(a,b):
    """Returns the sum of the inputs, 'a' and 'b' """
    return a + b

def mean(L):
    """ Returns the mean of the input list"""
    return float(reduce(add, L))/(float(len(L)))
  
def div(k):
    """ Takes integer input k, and then returns the remainder tested to see 
    if it is equal to 0. The result is either True or False"""
    return 42 % k == 0


def divides(n):
    """Takes input, n, and returns div(k) function"""
    def div(k):
        return n % k == 0
    return div


def prime(n):
    """takes a positive integer n and returns True or False depending on if the input 
    is prime or composite """
    if sum(map(divides(n), range(2, n-1))) > 0:
        return False
    return True

print(prime(12))
print(mean([1, 2, 3, 4]))




            
            
        







