import turtle

from world.obstacles import *


hal = turtle.Turtle()
hal.color('green')
hal.width(3)
hal.speed(0)

# draw rectangle
hal.penup()
hal.forward(100)
hal.right(90)
hal.pendown()
hal.forward(200)
hal.rt(90)
hal.fd(200)
hal.rt(90)
hal.fd(400)
hal.rt(90)
hal.forward(200)
hal.rt(90)
hal.fd(200)
hal.penup()
hal.home()
hal.lt(90)

# variables tracking position and direction
position_x = 0
position_y = 0
x = random.randint(-100,100)
y = random.randint(-200,200)
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    
    
def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y
       
 
def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """
    global position_x, position_y
    new_x = position_x
    new_y = position_y
    
    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    
    elif directions[current_direction_index] == 'right':   
        new_x = new_x + steps

    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps

    if is_position_allowed(new_x, new_y):
        if is_path_blocked(position_x, position_y, new_x, new_y) == False:
            position_x = new_x
            position_y = new_y
            return True
    
    return False


def exit():
    '''
    exit turtle
    '''
    
    turtle.Screen().bye()