'''
Created on Feb 21, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' jnelson6
'''
def fib(n):
    if n<= 1:
        return n
    return fib(n-1) + fib(n-2)

#for i in range(50):
#    print(i, fib(i))
    
def fib_memo(n):
    def fib_helper(n, memo):
        if n in memo:
            return memo[n]
        
        if n <= 1:
            result = n
        else:
            result = fib_helper(n - 1, memo) + fib_helper(n - 2, memo)
            
        memo[n] = result
        return result
    return fib_helper(n, {})

#for i in range(50):
#    print(i, fib_memo(i))

def LCS(S1, S2):
    '''Returns the length of the longest common subsequence in strings S1 and S2'''
    if S1 == ''  or S2 == '':
        return 0
    if S1[0] == S2[0] :
        return 1 + LCS(S1[1:], S2[1:])
    return max(LCS(S1, S2[1:]), LCS(S1[1:], S2))

def LCS_memo(S1, S2):
    def LCS_helper(S1, S2, memo):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        if S1 == ''  or S2 == '':
            result = 0
        elif S1[0] == S2[0]:
            result = 1 + LCS_helper(S1[1:], S2[1:], memo)
        else:
            result = max(LCS_helper(S1, S2[1:], memo), LCS_helper(S1[1:], S2, memo))
        memo[(S1, S2)] = result
        return result
    return LCS_helper(S1, S2, {})

#print(LCS_memo("asdfghjkl", "asdfghjkllll"))

def fast_LCS_with_values(S1, S2):
    '''returns a tuple containing the length of the longest common subsequence in 
    index 0 and the string in common in index 1'''
    def LCS_helper(S1, S2, memo):
        if (S1, S2) in memo:
            return memo[(S1, S2)]
        if S1 == ''  or S2 == '':
            result = (0, '')
        elif S1[0] == S2[0]:
            lose_both = LCS_helper(S1[1:], S2[1:], memo)
            result = (1 + lose_both[0], S1[0] + lose_both[1])
        else:
            useS1 = LCS_helper(S1, S2[1:], memo)
            useS2 = LCS_helper(S1[1:], S2, memo)
            if useS1[0] > useS2[0]:
                result = useS1 
            else:
                result = useS2
                
        memo[(S1, S2)] = result
        return result
    return LCS_helper(S1, S2, {})

#print(fast_LCS_with_values("asdfghjkl", "asdfghjkllll"))



