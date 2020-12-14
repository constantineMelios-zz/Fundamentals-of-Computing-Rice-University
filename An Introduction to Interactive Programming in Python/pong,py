# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
PAD_VEL = 5
paddle1_pos = [[HALF_PAD_WIDTH, HEIGHT // 2 - HALF_PAD_HEIGHT], [HALF_PAD_WIDTH, HEIGHT // 2 + HALF_PAD_HEIGHT]]
paddle2_pos = [[WIDTH - PAD_WIDTH // 2, HEIGHT // 2 - HALF_PAD_HEIGHT], [WIDTH - PAD_WIDTH // 2, HEIGHT // 2 + HALF_PAD_HEIGHT]]
paddle1_vel = 0
paddle2_vel = 0

# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists 
    ball_pos = [WIDTH //2, HEIGHT //2]
    if(direction == 'RIGHT'):
        ball_vel = [random.randrange(1, 2), -random.randrange(1, 3)]
    elif(direction == 'LEFT'):
        ball_vel = [-random.randrange(2, 4), -random.randrange(1, 2)]

# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel, LEFT, RIGHT  # these are numbers
    global score1, score2  # these are ints
    score1 = 0
    score2 = 0
    LEFT = not LEFT
    RIGHT = not RIGHT
    if(LEFT):
        spawn_ball('LEFT')
    else:
        spawn_ball('RIGHT')

def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0] += ball_vel[0]    
    ball_pos[1] += ball_vel[1]
    #top & bottom walls bouncing
    if(ball_pos[1] <= BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    elif(ball_pos[1] >= HEIGHT - BALL_RADIUS):
        ball_vel[1] = -ball_vel[1]
    #gutters touch
    if(ball_pos[0] <= BALL_RADIUS + PAD_WIDTH):
        if(paddle1_pos[0][1] <= ball_pos[1] <= paddle1_pos[1][1]):
            ball_vel[0] = -(ball_vel[0] * 1.10)
        else:
            score2 += 1
            spawn_ball('RIGHT')
    elif(ball_pos[0] >=  WIDTH - (BALL_RADIUS + PAD_WIDTH)):
        if(paddle2_pos[0][1] <= ball_pos[1] <= paddle2_pos[1][1]):
            ball_vel[0] = -(ball_vel[0] * 1.10)
        else:
            score1 += 1
            spawn_ball('LEFT')
        
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 3, "white", "white")
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_pos[0][1] + paddle1_vel >= 0 and paddle1_pos[1][1] + paddle1_vel <= HEIGHT):
        paddle1_pos[0][1] += paddle1_vel
        paddle1_pos[1][1] += paddle1_vel  
    if(paddle2_pos[0][1] + paddle2_vel >= 0 and paddle2_pos[1][1] + paddle2_vel <= HEIGHT):
        paddle2_pos[0][1] += paddle2_vel
        paddle2_pos[1][1] += paddle2_vel
    # draw paddles
    canvas.draw_polygon( paddle1_pos , PAD_WIDTH, 'white')
    canvas.draw_polygon( paddle2_pos, PAD_WIDTH, 'white')
    # determine whether paddle and ball collide    
    
    # draw scores
    canvas.draw_text(str(score1), [40,40], 40, 'white')
    canvas.draw_text(str(score2), [WIDTH - 40, 40], 40, 'white')
def keydown(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP['s']):
        paddle1_vel = PAD_VEL
    elif(key == simplegui.KEY_MAP['w']):
        paddle1_vel = -PAD_VEL
    if(key == simplegui.KEY_MAP['down']):
        paddle2_vel = PAD_VEL
    elif(key == simplegui.KEY_MAP['up']):
        paddle2_vel = -PAD_VEL
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if(key == simplegui.KEY_MAP['s']):
        paddle1_vel = 0
    elif(key == simplegui.KEY_MAP['w']):
        paddle1_vel = 0
    if(key == simplegui.KEY_MAP['down']):
        paddle2_vel = 0
    elif(key == simplegui.KEY_MAP['up']):
        paddle2_vel = 0

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', new_game, 100)


# start frame
new_game()
frame.start()
