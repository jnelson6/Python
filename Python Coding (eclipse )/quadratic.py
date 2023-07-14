'''
Created on Apr 19, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' 
jnelson6
'''
class QuadraticEquation(object):
    def __init__(self, a, b, c): #self gives you ability to reference inside class
        if a == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        else:
            self.__a = float(a)                 # double _ "__" means private variable
            self.__b = float(b)
            self.__c = float(c)
        
    @property
    def a(self):
        return self.__a
    
    @property
    def b(self):
        return self.__b
    
    @property
    def c(self):
        return self.__c
    
    def discriminant(self):
        return ((self.__b)**2) - (4 * self.__a * self.__c)
    
    def root1(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b + (self.discriminant() ** (1/2))) / (2 * self.__a)
    
    def root2(self):
        if self.discriminant() < 0:
            return None
        else:
            return (-self.__b - (self.discriminant() ** (1/2))) / (2 * self.__a)

    def __str__(self):  #operator overload
        s = ''
        if self.__a != 0:
            if self.__a == -1.0:
                s += '-x^2' + ' ' 
            if self.__a == 1.0:
                s += 'x^2' + ' ' 
            else:
                if self.__a > 0 and self.__a != 1.0:
                    s += str(self.__a) + 'x^2' + ' ' 
                if self.__a < 0 and self.__a != -1.0:
                    s += str(self.__a) + 'x^2' + ' ' 
        if self.__b != 0:
            if self.__b == 1.0:
                s += '+' + ' ' + 'x' + ' '
            if self.__b == -1.0:
                s += '-' + ' ' + 'x' + ' '
            else:
                if self.__b < 0 and self.__b != 1.0:
                    s += '-' + ' ' + str(0 - self.__b) + 'x' + ' '
                if self.__b > 0 and self.__b != 1.0:
                    s += '+' + ' ' + str(self.__b) + 'x' + ' '
            
        if self.__c != 0:   
            if self.__c < 0:
                s += '-' + ' ' + str(0 - self.__c) + ' '
            if self.__c > 0:
                s += '+' + ' ' + str(self.__c) + ' '
        return s + '= 0'
        
# print(QuadraticEquation(0,2,3))
