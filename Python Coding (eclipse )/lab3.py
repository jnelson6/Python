'''
Created on Feb 8, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' jnelson6
'''

def change(amount, coins):
    '''Takes in the amount of of money to be made and a list of the coins to 
    make the amount out of. coins always have the coin 1 in it. Returns a non
    negative number that indicates the least number of coins needed to make 
    the given amount'''
    if amount == 0:
        return 0
    if coins == []:
        return float('inf')
    if amount < 0:
        return float('inf')
    else:
        useit = change(amount - coins[0], coins) + 1
        loseit = change(amount, coins[1:])
    return min(useit, loseit)


    
