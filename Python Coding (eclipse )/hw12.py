'''
Created on Apr 27, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' 
jnelson6
'''
class Board(object):
    def __init__(self, width=7, height=6):
        '''Constructor for the objects of the game. takes in # of rows, # of columns'''
        self.height = height
        self.width =  width
        self.board = [[' ' for _ in range( width )] for _ in range( height )]

       
    def __str__(self):
        '''returns a string representing the called Board object. each "checker" 
        takes up one space, and all columns are separated by vertical bars (|). 
        The columns are labeled at the bottom.'''
        boardobject = ''
        for row in range(self.height):
            boardobject += '|'
            for col in range(self.width):
                boardobject += self.board[row][col] + '|'
            boardobject += '\n'
        boardobject += '-' * ((self.width + 1) * 2) + ' '
        return boardobject


    def allowsMove(self, col): 
        '''Checks that c is in the range(0, last column) and that there's 
        room left in the column. If move allowed return True. Return False if 
        no space available or not a valid column. '''
        columns = range(self.width)
        if col not in columns:
            return False
        colC = False
        for row in range(self.height):
            if self.board[row][col] == ' ':
                colC = True
        return colC
    
    def addMove(self, col, ox): 
        '''Checks the ox string variable that's "X" or "O", in column col. 
        It finds the highest row number available col and puts the checker 
        in that row. The highest row number available is the highest index 
        with ' ' in the column c. The highest row number corresponds to the 
        lowest physical row on the board.'''
        row = self.height - 1
        while self.board[row][col] != ' ':
            row -= 1
        self.board[row][col] = ox
             
 
         
    def setBoard( self, moveString ):
        ''' takes in a string of columns and places alternating checkers in 
        those columns, starting with 'X' For example, call b.setBoard('012345')
        to see 'X's and 'O's alternate on the bottom row, or b.setBoard('000000') 
        to see them alternate in the left column. moveString must be a string of 
        integers'''
        nextChecker = 'X' # start by playing 'X'
        for columnString in moveString:
            col = int(columnString)
            if 0 <= col <= self.width:
                self.addMove(col, nextChecker)
            if nextChecker == 'X': 
                nextChecker = 'O'
            else: nextChecker = 'X'
             
                
             
    def delMove(self,col): 
        '''"opposite" of addMove. Removes top checker from col. If column is empty, 
        do nothing.'''
        row = 0
        while self.board[row][col] == ' ' and row in range(self.height):
            row += 1
        if row != 6:
            self.board[row][col] = ' '
  

    
    def winsFor(self, ox): 
        '''Return True if the given ox-checker, 'X' or 'O', has won the calling Board. 
        Return False otherwise. Needs to check if the player has won horizontally, 
        vertically, or two ways diagonally'''  
       
    # checks if player won Horizontally 
        def Horizontal(ox, row, col):
            '''checks if player won horizontally'''
            def left(ox, row, col):
                '''checks left'''
                if col < 0:
                    return 0
                if self.board[row][col] != ox:
                    return 0
                return 1 + left(ox, row, col - 1)
            def right(ox, row, col):
                '''checks right'''
                if col == self.width:
                    return 0
                if self.board[row][col] != ox:
                    return 0
                return 1 + right(ox, row, col + 1)
            return left(ox, row, col) + right(ox, row, col) - 1 
        
    # checks if player won vertically 
        def Vertical(ox, row, col):
            '''checks if they player won vertically'''
            def above(ox, row, col):
                '''checks above'''
                if row < 0:
                    return 0
                if self.board[row][col] != ox:
                    return 0
                return 1 + above(ox, row - 1, col)
            def below(ox, row, col):
                '''checks below'''
                if row == self.height:
                    return 0
                if self.board[row][col] != ox:
                    return 0
                return 1 + below(ox, row + 1, col)
            return above(ox, row, col) + below(ox, row, col) - 1  
        
    # checks if player won diagonally
        def RightDiagonal(ox, row, col):
            '''checks if player won diagonally right'''
            def lowerR(ox, row, col):
                '''checks lower right'''
                if row == self.height or col == self.width:
                    return 0
                if self.board[row][col] != ox:
                    return 0
                return 1 + lowerR(ox, row + 1, col + 1)
            def upperL(ox, row, col):
                '''checks upper left'''
                if row < 0 or col  < 0:
                    return 0
                if self.board[row][col] != ox:
                    return 0
                return 1 + lowerR(ox, row - 1, col - 1)
            return lowerR(ox, row, col) + upperL(ox, row, col) - 1
        
    # checks if player won opposite diagonal
        def LeftDiagonal(ox, row, col):
            '''checks if player won diagonally left'''
            def upperR(ox, row, col):
                '''checks upper right'''
                if row < 0 or col == self.width:
                    return 0
                if self.board[row][col] != ox:
                    return 0
                return 1 + upperR(ox, row - 1, col + 1)
            def lowerL(ox, row, col):
                '''checks lower left'''
                if col < 0 or row == self.height:
                    return 0
                if self.board[row][col] != ox:
                    return 0
                return 1 + lowerL(ox,row+1,col-1)
            return upperR(ox, row, col) + lowerL(ox, row, col) - 1
        
        def Helper(self, ox, row, col):
            '''helper function to call all smaller functions'''
            if Horizontal(ox, row, col) >= 4 or Vertical(ox, row, col) >= 4 or LeftDiagonal(ox, row, col) >= 4 or RightDiagonal(ox, row, col) >= 4:
                return True
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == ox:
                    if Helper(self, ox, row, col) == True:
                        return True
        return False

    def hostGame( self ):
        '''This is a method that, when called from a connect four board object, will 
        run a loop allowing the user(s) to play a game. See below for an example user 
        interface'''
        print('Welcome to Connect Four!')
        win=False
        move='X'
        while win ==False:
            print(self)
            print()
            print(move + 's choice', end=' ')
            col=int(input())
            print('\n')
            if self.allowsMove(col) == True:
                self.addMove(col, move)
                win = self.winsFor(move)
                if win == True:
                    print(move + ' wins -- Congratulations!\n')
                if move == 'X':
                    move = 'O'
                else:
                    move = 'X'
            else:
                print('Nice try pick a different column')
                print()
        print(self)

b=Board(7,6)
b.hostGame()














