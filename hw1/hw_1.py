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
    return float(reduce(add, L)) / float(len(L))
#GO LOOK AT NOTES FOR THIS ONE
  
def div(k):
    return 42 % k == 0


def divides(n):
    def div(k):
        return n % k == 0
    return div

def prime(n):
    if sum(map(divides(n), range(2, n - 1))) > 0:
        return False
    return True
    

print(prime(12))
print(mean([1, 2, 3, 4]))