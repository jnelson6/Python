'''
Created on Mar 21, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' 
jnelson6
'''
def binToNum(S):
    '''takes in a binary string and returns the decimal integer'''
    if S == '':
        return 0
    elif S[-1] == '1':
        return binToNum(S[:-1])*2 + 1
    elif S[-1] == '0': 
        return binToNum(S[:-1])*2 + 0
    
def numToBin(n):
    '''Takes decimal integer and returns binary equivalent'''
    if n == 0:
        return ''
    elif n % 2 != 0:
        return numToBin(n//2) + '1'
    else:
        return numToBin(n//2) + '0'
    
def inverse(S):
    '''Changes bits in a binary string, 0->1, 1->0'''
    if S == '':
        return ''
    if S[0] == '1':
        return '0' + str(inverse(S[1:]))
    else:
        return '1' + str(inverse(S[1:]))
        
def TcToNum(S):
    '''Takes in a string of 8 bits that is in two's-complement Form
    and returns the corresponding integer'''
    if S == '00000000':
        return 0
    if S[0] == '0':
        result = (numToBin(binToNum(S)))
        return binToNum(result)
    elif S[0] == '1':
        result = inverse(numToBin( binToNum(S)))
        return -1 - binToNum(result)
    
def NumToTc(N):
    '''Takes in an integer and returns the twos complement string of 8 bits'''
    if N not in range(-128, 128):
        return 'Error'
    if N == -1:
        return inverse('0' * 7) + (numToBin(N * -1))
    if N < -1:
        N = N * -1
        result = inverse(numToBin(N - 1))
        return  '1' + result[-7:]
    if N <= 1:
        result = ('0' * 8) + numToBin(binToNum(inverse(numToBin(N + 1))))
        return result[-8:]
    else:
        result = ('1' * 8) + numToBin(binToNum(inverse(numToBin( N ))) + 1)
        return '0' + result[-7:]
