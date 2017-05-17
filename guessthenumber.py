# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math

num_range = 100

# helper function to start and restart the game
def new_game():
    range100()

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global count, secret_number, num_range
    secret_number = random.randrange(0, 100)
    count, num_range = 7, 100
    print "New game. Range is [0,100)"
    print "Number of remaining guesses is", count

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global count, secret_number, num_range
    secret_number = random.randrange(0, 1000)
    count, num_range = 10, 1000
    print "New game. Range is [0,1000)"
    print "Number of remaining guesses is", count
    print ""
    
def input_guess(guess):
    global secret_number, num_range, count
    player_guess = int (guess)
    print "Guess was", player_guess

    # conditions
    #ends game for have no more remaining guesses
    if count == -1:
            print "You ran out of guesses.  The number was", secret_number
            print ""
            if num_range == 100:
                #starts new game with range = 100
                range100()
            elif num_range == 1000:
                #starts new game with range = 100
                range1000()
            else:
                "ERROR!!!"
    # conditions and comparisons
    elif count <> -1:
        if secret_number == player_guess:
            count = 0
            print "Correct"
            print ""
            if num_range == 100:
                range100()
            elif num_range == 1000:
                range1000()
            else:
                "ERROR!!!"
        elif player_guess < 0 or player_guess >= num_range:
            print "Input out of range. Try another number"
            print ""
        elif secret_number < player_guess:
            count = count - 1
            print "Number of remaining guesses is", count
            print "Lower"
            print ""
        elif secret_number > player_guess:
            count = count - 1
            print "Number of remaining guesses is", count
            print "Higher"
            print ""
        else:
            "ERROR!!!"
    else:
        "ERROR!!!"
    
# create frame
f = simplegui.create_frame("Guess the number", 1, 200)

# register event handlers for control elements
f.add_button("Range is [0,100)", range100, 200)
f.add_button("Range is [0,1000)", range1000, 200)
f.add_input("Enter a guess", input_guess, 200)

#start frame
f.start()

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
