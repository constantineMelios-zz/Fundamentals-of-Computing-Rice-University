import simplegui
import random

range = 100
steps = 7

def new_game():
    global secret_number, steps, range
    if(range == 100):
        steps = 7
    else:
        steps = 9
    secret_number = random.randrange(0, range)
    print "New game! The range is [0, " + str(range) + ")"
    print "You have " + str(steps) + " guesses.\n"


def range100():
    global range, steps
    range = 100
    steps = 7
    new_game()
    

def range1000():
    global range
    range = 1000
    steps = 9
    new_game()
    
def input_guess(guess):
    global steps
    integer = int(guess)
    steps -= 1
    print "Guess was " + guess
    
    if(integer == secret_number):
        print "Correct\n"
        new_game()
    elif(steps == 0):
        print "You are out of guesses!\nThe number was " + str(secret_number) + "\n"
        new_game()
    elif(integer > secret_number):
        print "Guesses left: " + str(steps)
        print "Lower\n"   
    else:
        print "Guesses left: " + str(steps)
        print "Higher\n"
    

frame = simplegui.create_frame("Guess the number", 200, 300)

frame.add_input("input_guess", input_guess, 200)
frame.add_button("Range is [0,100)", range100, 200)
frame.add_button("Range is [0,1000)", range1000, 200)

new_game()
