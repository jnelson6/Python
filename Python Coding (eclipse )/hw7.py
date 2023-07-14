'''
Created on Mar 7, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' 
jnelson6
'''    
def numToBaseB(N, B):
    '''takes a non-neg integer N and a base B (between 2-10 inclusive) and 
    returns the string of the number N in base B '''
    if N == 0:
        return ''
    result = numToBaseB(N//B, B) + str(N % B)
    return str(result)

# When the file says return '' when N is 0, mine does BUT
#  the test cases given in the hw7 document say the result of 
# these 2 tests..
    # print(numToBaseB(0, 4))
    # print(numToBaseB(0, 2))
# ..should result in '0' not ''
#But that negates the rule of returning an empty string when N==0
    
def baseBToNum(S, B):
    '''takes a base B and a string S that is a number in base B. B is between
    2 and 10 inclusively. return the integer representation in base 10 '''
    counter = 0
    if S == '':
        return 0
    elif S[-1] == '0':
        result = 0
    elif S[-1] != '0':
        result = int(S[-1]) * (B ** counter)
    return result + baseBToNum(S[:-1], B) * B

def baseToBase(B1, B2, SinB1):
    '''Takes in 2 bases, B1 and B2, and string of a number in B1. Returns the result 
    of the number represented now with B2. Goes from B1 to num to B2'''
    return numToBaseB((baseBToNum(SinB1, B1)), B2)

def add(S,T):
    '''Takes 2 binary strings S, T, and returns the sum of them also in binary
    (converts both to decimal then adds and converts back to binary'''
    newNum = (baseBToNum(S, 2) + baseBToNum(T, 2))
    return numToBaseB(newNum, 2) 


def addB(S, T): 
    '''Takes 2 string inputs of binary numbers. Returns a new string representing
    the sum of the input strings. Sum found by binary addition algorithm NOT base
    conversions. Can be different lengths, no leading 0s'''
    if S == '':
        return T
    if T == '':
        return S
    def helper_addB(S,T):
        '''takes the input of 2 binary strings and adds the least-sig(right) terms
        and if there is a carry over, it adds the carry over with the next terms in that 
        index.'''
        if S[-1] == '0' and T[-1] == '0':
            return addB( S[:-1], T[:-1] ) + '0'
            
        if S[-1] == '1' and T[-1] == '0':
            return addB( S[:-1], T[:-1] ) + '1' 
            
        if S[-1] == '0' and T[-1] == '1':
            return addB( S[:-1], T[:-1] ) + '1'
            
        if S[-1] == '1' and T[-1] == '1':
            return addB('1', addB( S[:-1], T[:-1])) + '0'
    return helper_addB(S, T)



