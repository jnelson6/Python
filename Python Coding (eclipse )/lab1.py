'''
Created on Jan 26, 2018

@author: Julia Nelson
I pledge my honor that I have abided by the Stevens Honor System
'''

from cs115 import map, reduce
import math


def inverse(n):
    """Returns input n as its reciprocal"""
    return float( 1 / n )

def add(a, b):
    """Returns the sum of a and b."""
    return a + b 

def e(n):
    """Takes input n as a positive integer and approximates the value of e using a Taylor 
    expansion of n terms"""
    return reduce(add,(map(inverse, (map(math.factorial, range(n+1))))))
           
def error(n):
    """Returns the difference between actual value e and approximation 
    e(n)"""
    return abs(math.e - e(n))
    
