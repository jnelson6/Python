'''
Created on Mar 26, 2018

@author: Julia Nelson

'I pledge my honor that I have abided by the Stevens Honor System.' 
jnelson6
'''
import random

MAX_TRIES = 7

print("""--- Welcome to 'Guess My Number' ---

I'm thinking of a number between 1 and 100.
Try to guess the number in %d """ % MAX_TRIES, end='')
if MAX_TRIES == 1:
    print(" attempt...")
else:
    print(" attempts...")
    
# Set the initial values.
number = random.randint(1, 100)     #this still includes 100 because .randint is inclusive in its range
tries = 1
guess = int(input("Enter guess %d: " % tries))

# Guess loop
while guess != number:
    if guess > number:
        print("    Lower...")
    else:
        print("    Higher...")
    tries += 1
    if tries > MAX_TRIES:
        break
    guess = int(input("Enter guess %d: " % tries))
    
if tries <= MAX_TRIES:
    print("\nCongratulations! You correctly guessed the number %d, and it took you only %d" % (number, tries), end='')
        # \n means go to new line
    if tries == 1:
        print(" try!")
    else:
        print(" tries!")
else:
    print("\nSorry, you did not guess the number %d in %d" % (number, MAX_TRIES), end='')
    if tries == 1:
        print(" try.")
    else:
        print(" tries.")
                

