'''
Created on 2/26/18
@author:   Julia Nelson
Pledge:    'I pledge my honor that I have abided by the Stevens Honor System' 
            jnelson6

CS115 - Hw 5
'''
import turtle  # Needed for graphics

# Ignore 'Undefined variable from import' errors in Eclipse.

def sv_tree(trunk_length, levels):
    '''Takes in input of the trunk length and the number of levels of the tree
    returns the trace of the tree with the correct number of levels and each length 
    half the one before'''
    def treehelper(trunk_length, levels):
        '''helper function for sv_tree. Also changes colors and thickness of line'''
        if levels == 0:
            return
        turtle.bgcolor("light blue") #turns background light blue
        turtle.pensize(1.5 * levels) #makes the branch size get thinner as the levels change
        turtle.pencolor("brown") #turns pen to brown
        turtle.forward(trunk_length)
        turtle.left(45)
        treehelper(trunk_length / 2, levels - 1)
        turtle.right(90)
        treehelper(trunk_length / 2, levels - 1)
        turtle.left(45)
        turtle.back(trunk_length)
    turtle.left(90) #rotates entire tree upright
    treehelper(trunk_length, levels)
    turtle.done()


def fast_lucas(n):
    '''Returns the nth Lucas number using the memoization technique
    shown in class and lab. The Lucas numbers are as follows:
    [2, 1, 3, 4, 7, 11, ...]'''
    def lucas_helper(n, memo):
        '''Helper function to fast_lucas uses memoization'''
        if n in memo:
            return memo[n]
        if n == 0:
            result = 2
        elif n == 1:
            result = 1
        else:
            result = lucas_helper(n-1, memo) + lucas_helper(n-2, memo)
        memo[n] = result
        return result
    return lucas_helper(n, {})

def fast_change(amount, coins):
    '''Takes an amount and a list of coin denominations as input.
    Returns the number of coins required to total the given amount.
    Use memoization to improve performance.'''
    def fast_change_helper(amount, coins, memo):
        '''Helper function to fast_change uses memoization'''
        if (amount, coins) in memo:
            return memo[(amount, coins)]
        if amount == 0:
            result = 0
        elif coins == ():
            result = float('inf')
        elif amount < 0:
            result = float('inf')
        else:
            useit = fast_change_helper(amount - coins[0], coins, memo) + 1
            loseit = fast_change_helper(amount, coins[1:], memo)
            result = min(useit, loseit)
        memo[(amount, coins)] = result
        return result
    # Call the helper. Note we converted the list to a tuple.
    return fast_change_helper(amount, tuple(coins), {})

# If you did this correctly, the results should be nearly instantaneous.
print(fast_lucas(3))  # 4
print(fast_lucas(5))  # 11
print(fast_lucas(9))  # 76
print(fast_lucas(24))  # 103682
print(fast_lucas(40))  # 228826127
print(fast_lucas(50))  # 28143753123

print(fast_change(131, [1, 5, 10, 20, 50, 100]))
print(fast_change(292, [1, 5, 10, 20, 50, 100]))
print(fast_change(673, [1, 5, 10, 20, 50, 100]))
print(fast_change(724, [1, 5, 10, 20, 50, 100]))
print(fast_change(888, [1, 5, 10, 20, 50, 100]))

# Should take a few seconds to draw a tree.
sv_tree(100, 4)
