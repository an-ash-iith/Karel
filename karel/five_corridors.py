from karel.stanfordkarel import *

def main():
    """
    Traverses 5 variable length corridors and place beepers at the ends of them if there aren't already beepers there.
    """
    
    # pass  # Delete this line and write your code here! :)

    while(left_is_clear()):
        reverse_beeper()
        turn_left()
        move()
        turn_right()
    
    reverse_beeper()


def reverse_beeper():
    while(front_is_clear()):
        move()

    if(no_beepers_present()):
        put_beeper()
    

    turn_around()
    reverse_path()


def reverse_path():
    while(front_is_clear()):
       move()
    turn_around()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def turn_around():
    turn_left()
    turn_left()
    




# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
