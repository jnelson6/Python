'''
Created on 2/5/18
@author:   Julia Nelson and Amy Renne
Pledge:    'I pledge my honor that I have abided by the Stevens Honor System.'  
            jnelson6 arenne

CS115 - Hw 2
'''
import sys
from cs115 import map, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

def letterScore(letter, scorelist):
    '''Takes input of a single letter string and recurs over scoreList and 
    returns a list of the score of the letter'''
    if  scorelist == []:
        return 0
    if scorelist[0][0] == letter:
        return scorelist[0][1] 
    return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''iterate over a string and sum of the score of each letter's letterScores 
    of a word (adds the letter scores of a word '''
    if S == '':
        return 0
    return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)

def take_out(letter, Rack):
    '''Takes in a letter and a Rack. returns the list Rack without the letter '''
    if Rack == []:
        return []
    if Rack[0] == letter:
        return Rack[1:]
    else: 
        return [Rack[0]] + take_out(letter,Rack[1:])
    
def words_possible(word, Rack):
    '''Testing to the word against your rack. Can you make this input word with your
    input of rack '''
    if word == '':
        return True
    if word[0] in Rack:
        return words_possible(word[1:], take_out(word[0], Rack))
    else:
        return False
      
def add_word(word, scoreList):
    '''makes list of the word and the score'''
    return [word, wordScore(word, scoreList)]

def scoreList(Rack):
    '''What words can I make (with the rack that I have as an input)(words_possible)? Iterating 
    over the dictionary to see if your words can make any of those words. What is 
    the score of these words I can make? Then add them to a list.'''
    dictionary = Dictionary  #make variable so the global Dictionary isn't mutated
    return (map(lambda y: add_word(y, scrabbleScores), filter(lambda x: words_possible(x, Rack), dictionary)))

def top_num_scores(lst):
    if lst == []: 
        return ['', 0]
    elif lst[1:] ==[]:
        return lst[0]
    elif lst[0][1] >= lst[1][1]:
        lst[1] = lst[0]
    return top_num_scores(lst[1:])

def bestWord(Rack):
    '''iterate through the list of words you can make, Returns the highest scoring word from rack'''
    return top_num_scores(scoreList(Rack))

