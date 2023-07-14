'''
Created on Mar 22, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' 
jnelson6
'''
import random
import time

def map_sqr(lst):
    '''Returns a new list where every element in list has been squared'''
    new_list = []
    for value in lst:
        new_list.append(value * value)  # .append puts the squared number at the end of the list
    return new_list

# print(map_sqr([1,2,3]))

def factorial(n):
    '''takes in n returns factorial'''
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# for i in range(10):
#     print(i, factorial(i))

def fib(n):
    '''return fib of the number'''
    if n >= 0:
        a = c =0
    if n >= 1:
        b = c = 1    
    while n >= 2:
        c = a + b
        a = b
        b = c
        n -= 1
    return c

# for i in range(10):
#     print(1, fib(i))

def find_max(L):
    '''finds the max of a list'''
    if L == []:
        return None
    maxL = L[0]
    for x in L:
        if x > maxL:
            maxL = x 
    return maxL 

def find_min_max(L):
    '''finds the min and max of a list'''
    if L == []:
        return None
    maxL = minL = L[0]
    for x in L:
        if x > maxL:
            maxL = x
        elif x < minL:
            minL = x 
    return minL, maxL

def sequential_search(key, L):
    '''Returns the first index of key in L assuming
    the key exists in the list. If the key is not found,
    returns -1'''
    for i in range(len(L)):
        if L[i] == key:
            return i
    return -1

# finding the mid point of a set of numbers: (low + high)/2 take floor

def binary_search(key, L):
    low = 0
    high = len(L) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if key == L[mid]:
            return mid
        if key > L[mid]:
            low = mid + 1
        else:
            high = mid - 1
    return -low - 1

# Test cases for functions above 

# print(map_sqr([1,2,3]))
# for i in range(10):
#     print(i, factorial(i))
#     
# for i in range(10):
#     print(i, fib(i))
# 
# lst = [1, 2, 4, 7, 8, 10]
# for x in lst:
#     print(x, binary_search(x, lst))
# print(binary_search(3, lst))    

# big_list = [random.randint(1, 1000000) for _ in range(10000000)]
# start = time.clock()
# print(sequential_search(-2, big_list))
# print('%.2f ms' % ((time.clock() - start) * 1000))
# 
# big_list.sort()
# start = time.clock()
# print(binary_search(-2, big_list))
# print('%.2f ms' % ((time.clock() - start) * 1000))
#     

# alias
# A = [1, 2, 3]
# B = A
# B[0] = 0
# print(A)
# print(B)

# shallow copy

def shallow_copy(L):
    new_list = []
    for x in L:
        new_list.append(x)
    return new_list

# A = [1, 2, 3]
# B = shallow_copy(A)
# print(A)
# print(B)
# B[0] = 0
# print(A)
# print(B)

def deep_copy(L):
    new_list = []
    for x in L:
        if type(x) is list:
            new_list.append(deep_copy(x))
        else:
            new_list.append(x)
    return new_list

# A = [1, [2, 3], 4]
# B = shallow_copy(A)
# print(A)
# print(B)
# B[1][0] = -2
# print(A)
# print(B)

def sum_matrix(matrix):
    '''Returns the sum of all the values in a 2-dimensional list.
    Uses row and col indexes.'''
    total = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            total += matrix[row][col]
    return total

def sum_matrix2(matrix):
    '''Returns the sum of all the values in a 2-dimensional list.
    Uses the for each loops.'''
    total = 0
    for row in matrix:
        for x in row:
            total += x
    return total

#cell coord where the max is you need to keep track of col and row 
#so use sum_matrix(matrix)

# length of grid is usually row, col. 3 row by 4col matrix is len 3
def print_grid(grid):
    '''Formats a 3x3 matrix with ASCII art and prints it to the 
    screen.'''
    for row in range(len(grid)):
        print(' ', end='')
        for col in range(len(grid[row])):
            print(grid[row][col], end=' ')
            if col < 2:
                print('|', end=' ')
        print()
        if row < 2:
            print('-' * 11)

# Make a 3x3 grid of random integers between 1 and 9.
grid = [[random.randint(1, 9) for _ in range(3)] for _ in range(3)]

# print(grid)
# print(sum_matrix(grid))
# print(sum_matrix2(grid))
# print_grid(grid)

def swap(lst, i, j):
    '''swaps the i and j index values'''
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        if min_index != i:
            swap(lst, i, min_index)


# lst = [5, 1, 4, 2, 3]
# selection_sort(lst)
# print(lst)




    
    
    
    
    
