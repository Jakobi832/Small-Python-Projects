from turtle import *
fillcolor("light steel blue")
begin_fill()
setheading(0)
color("Black")
for square in range(4):
    forward(100)
    left(90)
    end_fill()
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

#legs
penup()
goto(knight_home)
fillcolor("Black")
setheading(0)
forward(8)
setheading(270)
forward(50)
begin_fill()
setheading(180)
forward(20)
setheading(90)
forward(30)
setheading(0)
forward(20)
setheading(270)
forward(30)
end_fill()

setheading(180)
forward(8)

fillcolor("White")

setheading(180)
forward(5)
begin_fill()
setheading(90)
forward(3)
setheading(270)
circle(3, -180)
setheading(270)
forward(3)
setheading(0)
forward(5)

end_fill()




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

penup()
goto(knight_home)
setheading(270)
forward(80/5)
setheading(0)
forward(-50/5)
# -55.00,-80.00
pendown()
color("black")
fillcolor("slate grey")

begin_fill()
setheading(230)
circle(200/5, 50)


speed("normal")
setheading(28)
circle(270/5, 25)

setheading(300)
circle(50, 25)

setheading(70)
circle(40, 50)
setheading(180)
forward(22)

setheading(300)
forward(20)
setheading(300 + 180)
forward(20)


end_fill()

fillcolor("gray")
begin_fill()
setheading(225)
forward(15/5)
setheading(135)
forward(50/5)
setheading(225)
forward(20/5)
setheading(135)
forward(-50/5)
setheading(225)
forward(25/5)
setheading(315)
forward(20/5)


end_fill()







hideturtle()
penup()
color("Black")
