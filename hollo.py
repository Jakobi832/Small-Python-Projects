from turtle import *

setup(500, 800)


color("Black")
title("Hollow Knight")
width(1)
bgcolor("light steel blue")



penup()
forward(50)
setheading(90)
forward(50)
knight_home = pos()



setheading(180)
forward(70/5)

pendown()
setheading(270)
penup()
forward(80/5)
pendown()

begin_fill()

penup()
setheading(0)
forward(27/5)
pendown()
forward(73/5)

circle(100/5, 90)
setheading(90)
forward(75/5)

#horn top right
setheading(30)
circle(80/5, 160)

width(0.7)

setheading(160)
circle(100/5, -20)

setheading(180)
circle(80/5, 14)

setheading(175)
circle(55/5 , -145)

#horn top right done
width(1)
setheading(180)
forward(220/5)
penup()
forward(20/5)
setheading(270)
forward(25/5)
pendown()

#horn top left

setheading(-30)
circle(80/5, -160)


setheading(-160)
circle(100/5, 20)

setheading(-180)
circle(80/5, -14)

setheading(-175)
circle(55/5 , 146)
#horn top left done

width(1)
penup()
setheading(180)
forward(20/5)
setheading(270)
forward(25/5)
pendown()

setheading(270)
forward(78/5)
setheading(270)
circle(100/5, 81)

fillcolor("white smoke")
end_fill()

width(1)

penup()
goto(knight_home)
setheading(0)
forward(70/5)
dot(75/5)
goto(knight_home)
setheading(180)
forward(70/5)
dot(75/5)
goto(knight_home)
pendown()


penup()
setheading(90)
forward(127/5.2)
setheading(270)
forward(26/5)

pendown()

fillcolor("white")
begin_fill()

color("white")
setheading(0)
circle(280/5, 20)
circle(280/5, -40)


setheading(0)
forward(195/5)
setheading(225)
forward(5/5)
end_fill()

###cheeck white parts
##width(2)
##penup()
##goto(knight_home)
##setheading(270)
##forward(73/5)
##setheading(0)
##forward(25/5)
##pendown()
##circle(100/5, 90)
##setheading(90)
##forward(60/5)
##
##penup()
##forward(13/5)
##setheading(0)
##
##pendown()
##setheading(30)
##circle(77/5, 90)
##
##
##
##penup()
##goto(knight_home)
##setheading(270)
##forward(73/5)
##setheading(0)
##forward(-25/5)
##pendown()
##circle(100/5, -90)
##setheading(90)
##forward(60/5)
##
##penup()
##forward(13/5)
##setheading(0)
##
##pendown()
##setheading(-30)
##circle(77/5, -90)
###end of cheeck white parts
penup()


speed("normal")
#start body
##width(4)
##
##penup()
##home()
##setheading(270)
##forward(80)
##setheading(0)
##forward(-50)
### -55.00,-80.00
##pendown()
##color("black")
##fillcolor("slate grey")
##
##begin_fill()
##setheading(230)
##circle(200, 55)
##
##setheading(28)
##circle(270, 25)
###(47,-78)
##penup()
##goto(47, -78)
##pendown()
##setheading(-230)
##circle(200, -57)
##
##setheading(-30)
##circle(270, -50)
##
##end_fill()
##penup()
##goto(47, -78)
##begin_fill()
##pendown()
##setheading(-230)
##circle(200, -57)
##setheading(-30)
##circle(270, -50)
##goto(47, -78)
##end_fill()
##
##penup()
##home()
##setheading(270)
##forward(80)
##pendown()
##setheading(0)
##forward(45)
##forward(-90)
##
##width(4)
###sword
##penup()
##goto(-55.00,-80.00)
##pendown()
##fillcolor("gray")
##begin_fill()
##setheading(225)
##forward(15)
##setheading(135)
##forward(50)
##setheading(225)
##forward(20)
##setheading(135)
##forward(-50)
##setheading(225)
##forward(25)
##setheading(315)
##forward(20)
##goto(-55.00,-80.00)
##end_fill()








#exit gracefully
hideturtle()
done()
