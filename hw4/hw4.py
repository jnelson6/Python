'''
Created on Feb 20, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' jnelson6
'''
def addrow(lst):
    ''''Given one row of pascal's triangle, generate the next row '''
    if len(lst) < 2:
        return [1]
    return [lst[0] + lst[1]] + addrow(lst[1:])

def pascal_row(n):
    '''Returns the nth row of pascal's triangle in a list'''
    if n == 0:
        return [1]
    if n == 1:
        return [1,1]
    return [1] + addrow(pascal_row(n-1))

def pascal_triangle(n):
    '''Takes in a number n and returns a list of lists of each row of pascals triangle 
    from 0 to n '''
    if n == 0:
        return [[1]]
    if n == 1:
        return [[1],[1,1]]
    return pascal_triangle(n-1) + [[1] + addrow(pascal_row(n-1))]

