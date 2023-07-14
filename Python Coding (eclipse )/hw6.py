'''
Created on 3/2/18
@author:  Julia Nelson and Amy Renne
Pledge:    'I pledge my honor that I have abided by the Stevens Honor System'
            jnelson6 arenne
CS115 - Hw 6
'''
# Number of bits for data in the run-length encoding format.
# The assignment refers to this as k.
COMPRESSED_BLOCK_SIZE = 5

# Number of bits for data in the original format.
MAX_RUN_LENGTH = 2 ** COMPRESSED_BLOCK_SIZE - 1

# Do not change the variables above.
# Write your functions here. You may use those variables in your code.

def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    else:
        return True
    
def numToBinary(n):
    '''Precondition: integer argument is non-negative. Returns the string with the binary representation 
    of non-negative integer n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s. Returns the integer corresponding to the binary 
    representation in s. Note: the empty string represents 0.'''
    if s == '':
        return 0
    elif s[-1] == '1':
        return binaryToNum(s[:-1])*2 + 1
    elif s[-1] == '0': 
        return binaryToNum(s[:-1])*2 + 0
    
def Pad_numToBinary(n):
    '''takes in integer. assume n is less than the compressed block size. pads out the num to binary of 
    the input and then pads it with the correct number of 0s'''
    s = numToBinary(n)
    return '0'*(COMPRESSED_BLOCK_SIZE - len(s)) + s

def prefixlength(s):
    '''Takes in a binary string and returns the length of the prefix. recursive to find length of the 
    prefix (until there is a 0) because you always want start with prefix of 0'''
    if len(s) == 1:
        return 1
    elif s[0] != s[1]:
        return 1
    return 1 + prefixlength(s[1:])

def compress(s):
    '''takes in a 64-bit binary number, breaks it into blocks, and alternates between 0s and 1s and gives
    you the number of 0s and 1s. Must start off with the number 0 so will have to add  phantom 0s if it 
    starts with 1'''
    def  helper_compress(s, b):
        '''B is an integer!! Helps to compress faster'''
        if s == '':
            return ''
        elif s[0] != chr(b + ord('0')):
            return Pad_numToBinary(0) + helper_compress(s,1-b)
        P_length = prefixlength(s)
        P_length = min(P_length, MAX_RUN_LENGTH)
        return Pad_numToBinary(P_length) + helper_compress(s[P_length:], 1-b)
    return helper_compress(s,0)

def uncompress(s):
    ''' inverts or undoes the compressing in your compress function.'''
    def helper_uncompress(s,b):
        '''Takes in a string of a compressed binary number. returns the original binary of the compressed 
        binary string. (reverses compress) '''
        if s == '':
            return ''
        n = binaryToNum(s[:COMPRESSED_BLOCK_SIZE])
        return str(b) * n + helper_uncompress(s[COMPRESSED_BLOCK_SIZE:], 1-b)
    return helper_uncompress(s, 0)

def compression(s):
    '''Write compression(S) to return the ratio of the compressed size to the original size for image S'''
    return len(compress(s)) / len(s)


#The compress function would use 64**5 number of bits. However if it were to start with 
#a 1 rather than a 0 it would add a prefix of 5 0's making the bits used 64**5 + 5 

# the tests that we conducted and the compression ratios that we found:

# Penguin = "00011000"+"00111100"*3 + "01111110"+"11111111"+"00111100"+"00100100"
# Smile = "0"*8 + "01100110"*2 + "0"*8 + "00001000" + "01000010" + "01111110" + "0"*8
# Five = "1"*9 + "0"*7 + "10000000"*2 + "1"*7 + "0" + "00000001"*2 + "1"*7 + "0"  
#
# print(compression(Penguin)) = 1.484375
# print(compression(Smile)) = 1.328125
# print(compression(Five)) = 1.015625
#
#our own image testing of the compression function
# print(compression('10101010010101')) = 5.0
# print(compression('1010')) = 6.25
# print(compression('1111111111111111111111111')) = 0.4
# print(compression('00000000000000000000000000000')) = 0.1724137931034483

# She is lai-ing because the output will not always be shorter than the input unless you 
# lose the order of the string. So if you lose the order of the string then you cannot uncompress
# the compressed string correctly. compressing the string '10101010101010101010' for us returns 
# a very long output. If she wanted to get a shorter output it would have to be out of the correct
# order of the string, returning '1'*10 and '0'*10




    