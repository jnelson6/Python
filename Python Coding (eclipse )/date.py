'''
Created on 4/22/18
@author:   Julia Nelson
Pledge:    'I pledge my honor that I have abided by the Stevens Honor System'
            jnelson6

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False
    
    def copy(self):
        '''Returns a new object with the same month, day, year
           as the calling object (self).'''
        dnew = Date(self.month, self.day, self.year)
        return dnew
    
    def equals(self, d2):
        '''Decides if self and d2 represent the same calendar date,
        whether or not they are the in the same place in memory.''' 
        return self.year == d2.year and self.month == d2.month and \
            self.day == d2.day
            
    def tomorrow(self):
#         DIM = (0,31,28,31,30,31,30,31,31,30,31,30,31)
        if DAYS_IN_MONTH[self.month] == self.day or self.month == 2 and self.day == 29:
            if self.month == 12:
                self.year += 1
                self.month = 1
                self.day = 1
            elif self.month == 2 and self.day == 28 and self.isLeapYear():
                self.day = 29
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1
    
    def yesterday(self):
        if self.day == 1:
            if self.month == 1:
                self.year -= 1
                self.month = 12
                self.day = 31
            else:
                self.month -= 1
                if self.month == 2 and self.isLeapYear():
                    self.day = 29
                else:
                    self.day = DAYS_IN_MONTH[self.month]
        else:
            self.day -= 1
        
    def addNDays(self, N):
        '''This method only needs to handle nonnegative integer inputs N. 
        Like the tomorrow method, this method should not return anything. 
        Rather, it should change the calling object so that it represents 
        N calendar days after the date it originally represented.'''
        print(self)
        for _ in range(N):
            self.tomorrow()
            print(self)
        
    def subNDays(self, N):
        ''' nonnegative integer input, N. This should not return anything. 
        Changes the calling object to represent N calendar days before 
        the date it originally represented. Use yesterday and a for loop'''
        print(self)
        for _ in range(N):
            self.yesterday()
            print(self)
    
    def isBefore(self, d2):
        '''This method should return True if the calling object is a 
        calendar date before input, d2. If self and d2 are the same day, 
        or if self is after d2, return False.'''
        if d2.year < self.year:
            return False
        if d2.year == self.year and d2.month < self.month:
            return False
        if d2.year == self.year and d2.month == self.month and d2.day < self.day:
            return False
        if self.equals(d2):
            return False
        return True
    
    def isAfter(self, d2):
        '''Return True if the calling object is a date after the d2. 
        If self and d2 are the same day or if self is before d2, return False. '''
        if self.equals(d2):
            return False
        return not self.isBefore(d2)
    
    def diff(self, d2):
        if self.equals(d2):
            return 0
        original_date = self.copy()
        target_date = d2.copy()
        if original_date.isAfter(target_date):
            days = 0
            while target_date.isBefore(original_date):
                target_date.tomorrow()
                days += 1
        else:
            days = 0
            while original_date.isBefore(target_date):
                original_date.tomorrow()
                days -= 1
        return days
    
    def dow(self):
        days = ['Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'Monday', 'Tuesday']
        wednesday = Date(11, 9, 2011)
        difference = self.diff(wednesday)
        return days[difference % 7]
    
        
        
        
        


