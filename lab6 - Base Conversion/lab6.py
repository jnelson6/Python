'''
Created on 3/2/18
@author:   Julia Nelson
Pledge:   'I pledge my honor that I have abided by the Stevens Honor System'
        jnelson6

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    else:
        return True
#complete base-2 representation of 42 is 
#101010

#Given an odd base-10 the right most bit in base-2 will be 1, if its even it will be 0.
#Odd numbers will need to use the 2**0 for the remainder of 1 

# Removing the right most bit from a number like 1010 or 1011 returns its decimal 
# representation //2 . So 1010 is 10 and 1011 is 11 and 101 is 5. 10 // 2 = 5 
# and 11 // 2 = 5

# If N is odd and we have the base-2 respresentation of Y, N's base-2 is Y's with a 1 
#added to the right side
# If N is even and we have the base-2 respresentation of Y, N's base-2 is Y's with a 0 
#added to the right side
#This is because the right most represents the decimal num 1 

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '1':
        return binaryToNum(s[:-1])*2 + 1
    elif s[-1] == '0': 
        return binaryToNum(s[:-1])*2 + 0


def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    n = binaryToNum(s) + 1
    x = numToBinary(n)
    return ('0'*(8 - len(x)) + x)[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    print(s)
    if n == 0:
        return
    else:
        (count(increment(s), n-1))

 
#ternary rep of 59 is 2012 because it contains two(2) 27's which is 54, 
#then it doesn't contain any 9's because the remainder is 5 so ther is a 0.
#in the remainder 5 it contains one 3, with a remainder of 2. so two ones
# making it 2012

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    else:
        return numToTernary(n//3) + str(n%3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '2':
        return ternaryToNum(s[:-1])*3 + 2
    elif s[-1] == '1':
        return ternaryToNum(s[:-1])*3 + 1
    elif s[-1] == '0': 
        return ternaryToNum(s[:-1])*3 + 0



