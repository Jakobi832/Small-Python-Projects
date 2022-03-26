#stay at home

from turtle import *
from random import randint

#setup canvas
setup()
title("Quite simple, really")
bgcolor("light grey")


#createa home for the turtle
dot(15)

#create the turtle

shape("turtle")
color("green")
turtlesize(2)
width(3)
pendown()
setheading(randint(0,359))

#function to decide if we are too far from home
def too_far():
    return distance(0, 0) > 300

#move the turtle
for step in range(100):
    # turn around if too far from home and change color depending on its heading
    if too_far():
        left(20)
        color("red")
    else:
        left(randint(-20, 20))
        color("green")
    #draw a dotted line by changing the pen up/down
    if isdown():
        penup()
    else:
        pendown()
    #walk one step
    forward(10)
#go home, turtle
penup()
color("green")
home()

#exit gracefully
done()
