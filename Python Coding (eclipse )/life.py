#
# life.py - Game of Life lab
#
# Name: Julia Nelson
# Pledge: "I pledge my honor that I have abided by the Stevens Honor System"
# jnelson6

import random
import sys

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )
        
def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells."""
    A = createBoard( width, height )
    
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
 
def innerCells(w,h):
    '''which returns a 2d array of all live cells - with the 
    value of 1 - except for a one-cell-wide border of empty 
    cells (with the value of 0) around the edge of the 2d array'''
    A = createBoard(w, h)

    for row in range(h):
        for col in range(w):
            if 0 < row < h-1 and 0 < col < w-1:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def randomCells( w, h ):
    ''' returns an array of randomly-assigned 1's and 0's 
    except that the outer edge of the array is still 
    completely empty (all 0's)'''
    A = createBoard(w, h)
    for row in range(h):
        for col in range(w):
            if 0 < row < h - 1 and 0 < col < w - 1:
                A[row][col] = random.choice([0, 1])
    return A

def copy (A):
    '''make a deep copy of the 2d array A. Thus, copy will 
    take in a 2d array A and it will output a new 2d array 
    of data that has the same pattern as the input array'''
    width = len(A[0])
    height = len(A)
    B = createBoard(width, height)
    for row in range(height):
        for col in range(width):
            B[row][col] = A[row][col]
    return B

def innerReverse( A ):
    '''that takes an old 2d array (or "generation") and then
    creates a new generation of the same shape and size '''
    rev = copy( A )
    for row in range(len(A)):
        for col in range(len(A[0])):
            if row == 0 or col==0:
                rev[row][col] = 0
            elif row == (len(A)-1) or col == (len(A[0])-1):
                rev[row][col] = 0
            else:
                if rev[row][col] == 0:
                    rev[row][col] = 1
                elif rev[row][col] == 1:
                    rev[row][col] = 0
    return rev

def countNeighbors(row, col, A):
    '''returns the number of live neighbors (1s) for a cell 
    in the board A at a particular row and col.'''
    count = 0
    if A[row][col - 1] != 0: # left neighbor
        count += 1
    if A[row][col + 1] != 0: # right neighbor
        count += 1
    if A[row - 1][col] != 0: # above neighbor 
        count += 1
    if A[row + 1][col] != 0: # below neighbor
        count += 1
    if A[row - 1][col - 1] != 0: #top left diagonal neighbor 
        count += 1
    if A[row - 1][col + 1] != 0:  #top right diagonal neighbor
        count += 1
    if A[row + 1][col - 1] != 0: #bottom left diagonal neighbor
        count += 1
    if A[row + 1][col + 1] != 0: #bottom right diagonal neighbor
        count += 1 
    return count

def next_life_generation( A ):
    """ makes a copy of A and then advanced one generation 
    of Conway's game of life within the *inner cells* of 
    that copy. The outer edge always stays 0."""
    height = len(A)
    width = len(A[0])
    newA = copy(A)
    for i in range(1,height - 1):
        for j in range(1,width - 1):
            alive = countNeighbors(i, j, A)
            if alive < 2 or alive > 3:
                newA[i][j] = 0
            elif alive == 3:
                newA[i][j] = 1
    return newA



