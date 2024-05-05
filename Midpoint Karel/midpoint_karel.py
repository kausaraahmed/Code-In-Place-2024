from karel.stanfordkarel import *


def main():
    # go to the top right corner of the world
    go_to_top_right_point()
    go_to_right()

    # face right so that checks can be made if the front is clear or not
    turn_right()

    # until karel reaches the floor of the world
    while front_is_clear():
        # step down from the position
        step_down()

        # if karel does not reach the floor then go a more step down
        if front_is_clear():
            move()

    turn_left()  # turn left to get in the proper position
    put_beeper()  # place the beeper on the middle point


def step_down():
    move()
    turn_right()
    move()
    turn_left()


def go_to_top_right_point():
    # go to the top-most point
    turn_left()
    while front_is_clear():
        move()
    turn_right()

    # go to the right-most point
    while front_is_clear():
        move()


# let the karel move in the right direction
def turn_right():
    turn_left()
    turn_left()
    turn_left()


if __name__ == '__main__':
    main()
