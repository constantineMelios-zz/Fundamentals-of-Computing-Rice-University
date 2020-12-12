import random

def name_to_number(name):
    if(name == 'rock'):
        return 0
    elif(name == 'Spock'):
        return 1
    elif(name == 'paper'):
        return 2
    elif(name == 'lizard'):
        return 3
    elif(name == 'scissors'):
        return 4
    else:
        print "Wrong input. Please enter rock, paper, scissors, lizard, or Spock"


def number_to_name(number):
    if(number == 0):
        return 'rock'
    elif(number == 1):
        return 'Spock'
    elif(number == 2):
        return 'paper'
    elif(number == 3):
        return 'lizard'
    elif(number == 4):
        return 'scissors'
    else:
        print "Wrong input, expected an integer n, 0 <= n <= 4"


    

def rpsls(player_choice): 
    print "\n"
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    
    comp_number = random.randrange(0, 5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    
    result = (comp_number - player_number) % 5
    
    if result == 0:
        print "Player and computer tie!"
    elif result < 3:
        print "Computer wins!"
    else:
        print "Player wins!"
 
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
