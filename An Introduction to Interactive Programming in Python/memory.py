# implementation of card game - Memory

import simplegui
import random

card_width = 50
card_height = 100
memory_deck = []

# helper function to initialize globals
def new_game():
    global memory_deck, state, turn, pair
    state = 0
    turn = 0
    label.set_text("Turns: " + str(turn)) 
    pair = []
    memory_deck = []
    numbers = range(8) + range(8)
    random.shuffle(numbers)
    for number in numbers:
        memory_deck.append({"number": number, "is_revealed": False})
     
# define event handlers
def mouseclick(pos):
    global state, pair, turn, label
    card = memory_deck[pos[0] // 50]
    if not card['is_revealed'] == True:
        if(len(pair) == 2):
            check_similarity()
        if state == 0:
            state = 1
        elif state == 1:
            turn += 1
            label.set_text("Turns: " + str(turn))
            state = 2
        elif state == 2:
            state = 1
        pair.append(card)
        card['is_revealed'] = True
    
def check_similarity():
    global pair
    if not pair[0]['number'] == pair[1]['number']:
        for card in memory_deck:
            if card == pair[0] or card == pair[1]:
                card['is_revealed'] = False
    pair = []
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    counter = 0
    for card in memory_deck:
        if card["is_revealed"] == True:
            canvas.draw_text(str(card['number']), [counter * card_width + 15, 65], 40, 'White')
        else:
            canvas.draw_polygon([(counter * card_width, 0),((counter + 1) * card_width, 0),((counter + 1) * card_width, card_height),((counter + 1) * card_width, card_height),(counter * card_width, card_height)], 5, "Black", "Green", ) 
        counter += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
