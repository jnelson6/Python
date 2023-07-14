'''
Created on Apr 20, 2015
Last modified on April 15, 2017

@author: Brian Borowski

CS115 - Student class with Python decorators.
'''
import sys

class Student(object):
    def __init__(self, first_name, last_name, sid, gpa): #self gives you ability to reference inside class
        self.__first_name = first_name                  # double _ "__" means private variable
        self.__last_name = last_name
        self.__sid = sid
        self.__anxiety_level = 100
        # The line below actually calls @gpa.setter, eliminating the need for
        # duplicating the error checking. As long as self.__gpa is created
        # before the constructor finishes executing, all is well.
        self.gpa = gpa          # calling the setter from within the constructor
        
    @property
    def anxiety_level(self):
        return self.__anxiety_level
    
    @anxiety_level.setter
    def anxiety_level(self, anxiety_level):
        if anxiety_level< 0 or anxiety_level > 100:
            raise ValueError('Anxiety level must be between 0 and 100.') # using private and setting a method stops you from being able
        self.__anxiety_level = anxiety_level                            # to make it a number outside the constraint of 100. Sets checking and boundaries 
                                                # Method to make sure what you're passing in is valid. 

    @property                   # decorator for a private member variable. Makes the private variable readable outside
    def first_name(self):       # the class. Getter/accessor
        return self.__first_name                

    @first_name.setter                  # decorator for giving you the ability to modify the value of a private member
    def first_name(self, first_name):   # variable. Setter/Mutator Note: you cannot have a setter w/o the corresponding 
        self.__first_name = first_name  # @property

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name):
        self.__last_name = last_name

    @property
    def sid(self):
        return self.__sid

    @sid.setter
    def sid(self, sid):
        self.__sid = sid

    @property
    def gpa(self):
        '''This is an accessor or getter method. If you have a reference, s1,
        to a Student object, simply READ the value of the gpa by referencing
        s1.gpa.'''
        return self.__gpa

    @gpa.setter
    def gpa(self, gpa):
        '''This is a mutator or setter method. If you have a reference, s1,
        to a Student object, simply ASSIGN the value of the gpa as in,
        s1.gpa = 3.75.'''
        try:
            local_gpa = float(gpa)
        except:
            raise TypeError('GPA must be a float.')
        if local_gpa < 0.0 or local_gpa > 4.0:
            raise ValueError('GPA must be between 0.0 and 4.0.')
        self.__gpa = local_gpa

    def __str__(self):  #technically an operator overload
        return self.__first_name + ' ' + self.__last_name + ' (SID: ' + \
            self.__sid + ', GPA: ' + str(self.__gpa) + ')'

if __name__ == '__main__':
    try:
        s1 = Student('John', 'Doe', '123456', '4.0')  # Calls __init__
    except TypeError as error:
        print('Error:', error)
        sys.exit(1)
    print(s1)  # Calls __str__
    try:
        s1.gpa = input('Enter new GPA: ').strip()  # Calls setter
    except (TypeError, ValueError) as error:
        print('Error:', error)
        sys.exit(1)
    print('Student GPA changed to:', s1.gpa)  # Calls property
    print(s1)  # Calls __str__
