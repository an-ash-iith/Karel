"""
This is a worked example. This code is starter code; you should edit and run it to 
solve the problem. You can click the blue show solution button on the left to see 
the answer if you get too stuck or want to check your work!
"""

from karel.stanfordkarel import *

def main():
    """
    Place beepers in the bottom row of a world with 3 slots.
    """
    
    # pass # Delete this line and write your code here! :)

    for i in range(2):

     finish_work()
     move()

    finish_work()


def finish_work():
    turn_right()
    move()
    put_beeper()
    turn_around()
    move()
    turn_right()

def turn_right():
    for i in range(3):
       turn_left()

def turn_around():
    for i in range(2):
       turn_left()

# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()