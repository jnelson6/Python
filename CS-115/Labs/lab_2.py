'''
Created on Feb 3, 2018

@author: Julia Nelson

I pledge my honor that I have abided by the Stevens Honor System.
'''

def dot(L, K):
    '''takes input of equal length lists, L and K, that contain numeric 
    values only and returns the dot product(the sum of the products of 
    the that are in the same position in the lists'''
    if L == [ ] or K == [ ]:            #if both lists are empty return 0.0
        return 0.0
    else: 
        result = L[0] * K[0]            #Multiplying the first terms 
        return result + dot(L[1:],K[1:])#result of first term added 
                                        #dot of the next terms in list


def explode(S):
    '''takes string input and returns each character as individual string
    in a list'''
    if S == '' :    #if the string has no characters return an empty list
        return []
    else:  
        return list(S[0])+explode(S[1:])
    
def ind(e, L):
    '''Take in an element, e, and either list or string, L, and returns
    the index where e is first found in L'''
    index=1
    if L == []:
        return 0
    if e != L[0]:
        return index +ind(e, L[1:])
    elif e == L[0]:
        return index 
    return index

def removeAll(e, L):
    '''Takes element, e, list, L, and returns L with all top-level elements 
    equal to e removed. (top-level means not in another element in L)'''
    if L == []:
        return [] 
    if e != L[0]:
        return [L[0]] + removeAll(e, L[1:])
    if e == L[0]:
        return removeAll(e, L[1:]) 

def myFilter(f, L):
    '''Takes input of function, f, and list, L. Returns new list with only
    the elements of L that satisfy function f and result in True'''
    if L == []:
        return []
    if f (L[0]) == True:
        return [L[0]] + myFilter(f, L[1:])
    else:
        if f (L[0]) == False:
            return myFilter(f, L[1:])

def deepReverse(L): 
    '''Take a list as input and reverses its elements... if element in the 
    input is another list, it is also reversed'''
    #if isinstance(L, list):
    if L == []:
            return []
    else:
        if isinstance(L[0], list):
            return deepReverse(L[1:]) + [deepReverse(L[0])]
        else:                       
            return deepReverse(L[1:]) + [L[0]]

#test
print(deepReverse([1, [2, [3, 4], [5, [6, 7], 8]]]))
