'''
Created on Feb 21, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' jnelson6
'''
import turtle

def square_spiral(walls):
    def square_spiral_helper(walls, distance, initial, count):
        if walls == count:
            turtle.done()
        else: 
            turtle.left(90)
            turtle.forward(distance)
            square_spiral_helper(walls, distance + initial * (count % 2), initial, count + 1)
    square_spiral_helper(walls, 20, 20, 0)

def octogonal_spiral(walls):
    def octogonal_spiral_helper(walls, distance, initial, count):
        if walls == count:
            turtle.done()
        else: 
            turtle.left(45)
            turtle.forward(distance)
            octogonal_spiral_helper(walls, distance + initial * (count % 2), initial, count + 1)
    octogonal_spiral_helper(walls, 20, 5, 0)
    
octogonal_spiral(30)