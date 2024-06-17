from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
    # pass

    for i in range(3):
        climb_hurdle()
        for j in range(4):
         move()

    climb_hurdle()
 

def climb_hurdle():
    turn_left()
    while(front_is_clear()):
        put_beeper()
        move()
    put_beeper()
    descent_hurdle()


def descent_hurdle():
    turn_around()

    while(front_is_clear()):
        move()

    turn_left()

def turn_right():
    
    for i in range(3):
        turn_left()

def turn_around():
    for i in range(2):
        turn_left()

if __name__ == '__main__':
    main()