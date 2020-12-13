# template for "Stopwatch: The Game"

import simplegui

# define global variables
app_time = 0
is_running= False
total_tries = 0
succesful_tries = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    ms = str(t % 10)
    if(((t - (t % 10)) / 10) % 60 < 10):
        sec = "0" + str(((t - (t % 10)) / 10) % 60)
    else:
        sec = str(((t - (t % 10)) / 10) % 60)
    min = str(t // 600)
    return min + ":" + sec + "." + ms
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global timer, is_running
    timer.start()
    is_running = True

def stop():
    global timer, is_running, total_tries, succesful_tries
    timer.stop()
    if(is_running):
        total_tries += 1
        if(app_time % 10 == 0):
            succesful_tries += 1
    is_running = False
    
def reset():
    global app_time, timer, is_running, total_tries, succesful_tries
    timer.stop()
    is_running = False
    app_time = 0
    total_tries = 0
    succesful_tries = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global app_time
    app_time += 1 

# define draw handler
def draw(canvas):
    canvas.draw_text(format(app_time), [110,110], 35, 'white', 'sans-serif')
    canvas.draw_text(str(succesful_tries) + "/" + str(total_tries), [250, 40], 20, 'green', 'sans-serif')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 200)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)
timer = simplegui.create_timer(100, tick)

# register event handlers


# start frame
frame.start()

# Please remember to review the grading rubric
