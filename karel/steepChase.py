"""
File: SteepleChaseKarel.py
--------------------------
Karel runs a steeple chase that is 9 avenues long.
Hurdles are of arbitrary height and placement.
"""

from karel.stanfordkarel import *

def main():
    for i in range(8):    #have to go exactly 8 steps 
      if front_is_clear():
         move()
      else:
         cross_hurdle()


def cross_hurdle():
   ascend_hurdle()
   turn_right()
   move()
   turn_right()
   descend_hurdle()
   turn_left()

def ascend_hurdle():
   turn_left()
   while(right_is_blocked()):
      move()
   
  
def descend_hurdle():
   
   while(front_is_clear()):
      move()


def turn_right():
   turn_left()
   turn_left()
   turn_left()     


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
