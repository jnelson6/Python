'''
Created on Apr 18, 2012

@author: bribor
'''
from abc import ABCMeta, abstractproperty

class Shape(metaclass=ABCMeta):
    def __init__(self, x, y, name="Shape"):
        self.__name = name
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter       # cannot have a setter by itself.. must have property before it, but prop can be alone without setter
    def y(self, y):
        self.__y = y

    @abstractproperty       #we don't know the shape yet so we don't know, but it shows that you have to do it
    def area(self):     # pushes all the base x y and name up to base class so you dont have to duplicate the code for each shape
        pass

    def __str__(self):  #it is an override, takes member variables that prints a readable representation
        return self.__name + " at (" + str(self.__x) + ", " + \
               str(self.__y) + ")"

if __name__ == '__main__':
    try:
        a = Shape(10, 20)
    except TypeError as error:
        print("Error: " + str(error))
