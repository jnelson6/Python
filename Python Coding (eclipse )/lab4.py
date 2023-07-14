'''
Created on Feb 15, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' jnelson6
'''

def knapsack(capacity, itemList):
    '''takes in the capacity of your knapsack and the list of items and 
    returns both the maximum value and the list of items without exceeding 
    the given capacity of the knapsack'''
    if capacity == 0 or itemList == []:
        return [0, []]
    if itemList[0][0] > capacity :
        return knapsack(capacity, itemList[1:])
    use_it = knapsack(capacity - itemList[0][0], itemList[1:])
    lose_it = knapsack(capacity, itemList[1:])
    Sum = use_it[0] + itemList[0][1]
    if Sum > lose_it[0]:
        return [Sum, [itemList[0]] + use_it[1]]
    return lose_it
    
                