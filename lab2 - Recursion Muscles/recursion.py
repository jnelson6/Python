'''
Created on Jan 30, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' jnelson6
'''

from cs115 import map, range, reduce
import math

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def tower(n):
    ''' to the power of 2 however many n times'''
    if n == 0:
        return 1
    return 2 ** tower(n-1)

def tower_reduce(n):
    '''Computes 2^(2^(2)) with n twos, using reduce'''
    def power(x, y):
        return y ** x 
    return reduce(power, [2] * n)

def length(lst):
    ''' Returns the length of the list.'''
    if lst == []:
        return 0
    return 1 + length(lst[1:])

def reverse(lst):
    ''' Takes as input, a list of elements,  and returns them in reverse order'''
    if lst == []:
        return []
    return reverse(lst[1:]) + [lst[0]]
    
def member(x, lst):
    ''''returns True is x is contained in the list and False otherwise'''
    if lst == []:
        return False
    if x == lst[0]:
        return True
    return member(x, lst[1:])
        
def my_map(f, lst):
    '''Returns a new list where the function f has been applied to every element in the original list'''
    if lst == []:
        return []
    return [f(lst[0])] + my_map(f, lst[1:])

def sqr(x):
    return x * x

def my_reduce(f, lst):
    '''Reduces the list to a single value as dictated by the predicate function'''
    def my_reduce_helper(f, lst, accum):
        if lst == []:
            return accum
        return my_reduce_helper(f, lst[1:], f(accum, lst[0]))
    if lst == []:
        raise TypeError('my_reduce() of empty sequence with initial value')
    return my_reduce_helper(f, lst[1:], lst(0))
    
    
def prime(n):
    '''Return whether or not an integer is prime'''
    possible_divisors = range(2, int(math.sqrt(n)) + 1)
    divisors = filter(lambda x: n % x == 0, possible_divisors)
    return len(divisors) == 0
    
def primes(n):
    def sieve(lst):
        if lst == []:
            return []
        return [lst[0]] + sieve(filter(lambda x: x % lst[0] != 0, lst[1:]))
    return sieve(range(2, n +1))

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)















