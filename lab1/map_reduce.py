'''
Created on Jan 25, 2018

@author: Julia
'''
from cs115 import reduce


def add(a, b):
    """Returns the sum of a and b."""
    return a + b 

def sqr(x):
    """Returns the square of x"""
    return x * x

def span(lst):
    """Returns the difference between the maximum and minimum numbers in a
    list. """
    return reduce(max, lst) - reduce(min, lst)
    
def gauss(n):
    """Takes as input a positive integer n and returns the sum
    1 + 2 + 3 + ... + n """
    
    return reduce(add, range(1, n+1))
    
def sum_of_squares(n):
    """Takes as input a positive integer n and returns the sum
    1^2 + 2^2 +3^2 +... +n^2."""
    return reduce(add, map(sqr, range(1, n+1)))

print(span([3, 1, 42, 7, -1]))
