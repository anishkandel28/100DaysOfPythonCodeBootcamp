#hurdle 1 using for loop and function

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()  
    turn_left()
    
for steps in range(6):
    jump()
 
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
