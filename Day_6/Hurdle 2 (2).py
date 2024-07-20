
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
       
while not at_goal():
    Circle()




################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
