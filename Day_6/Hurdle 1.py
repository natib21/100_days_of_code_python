
def turn_round():
    turn_left()
    turn_left()
    turn_left()
def jumpUp():
    turn_left()
    move()
    turn_round()
def Circle():   
    move()
    jumpUp()
    move()
    turn_round()
    move()
    turn_left()
number_hurdle = 6
while number_hurdle > 0:
    Circle()
    number_hurdle = number_hurdle - 1
    








################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
