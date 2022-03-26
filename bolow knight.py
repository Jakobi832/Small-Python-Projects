from turtle import *

setup(500, 800)
color("Black")
title("Hollow Knight")
width(4)
speed("fastest")
bgcolor("light steel blue")


penup()
setheading(180)
forward(70)

pendown()
setheading(270)
penup()
forward(80)
pendown()

begin_fill()

penup()
setheading(0)
forward(27)
pendown()
forward(73)

circle(100, 90)
setheading(90)
forward(75)

#horn top right
setheading(30)
circle(80, 160)

width(2.5)

setheading(160)
circle(100, -20)

setheading(180)
circle(80, 14)

setheading(175)
circle(55 , -145)

#horn top right done
width(4)
setheading(180)
forward(220)
penup()
forward(20)
setheading(270)
forward(25)
pendown()

#horn top left

setheading(-30)
circle(80, -160)

width(2.5)

setheading(-160)
circle(100, 20)

setheading(-180)
circle(80, -14)

setheading(-175)
circle(55 , 146)
#horn top left done

width(4)
penup()
setheading(180)
forward(20)
setheading(270)
forward(25)
pendown()

setheading(270)
forward(78)
setheading(270)
circle(100, 81)

fillcolor("white smoke")
end_fill()

width(3)

penup()
home()
forward(70)
dot(75)
home()
setheading(180)
forward(70)
dot(75)
home()
pendown()


penup()
setheading(90)
forward(127)


setheading(270)
forward(26)

pendown()

fillcolor("white")
begin_fill()

color("white")
setheading(0)
circle(280, 20)
circle(280, -40)


setheading(0)
forward(195)
setheading(225)
forward(5)
end_fill()

#cheeck white parts
width(6.2)
penup()
home()
setheading(270)
forward(73)
setheading(0)
forward(25)
pendown()
circle(100, 90)
setheading(90)
forward(60)

penup()
forward(13)
setheading(0)

pendown()
setheading(30)
circle(77, 90)



penup()
home()
setheading(270)
forward(73)
setheading(0)
forward(-25)
pendown()
circle(100, -90)
setheading(90)
forward(60)

penup()
forward(13)
setheading(0)

pendown()
setheading(-30)
circle(77, -90)
#end of cheeck white parts
penup()
color("white smoke")
goto(-130, 110)
pendown()
goto(-130, 120)


#start body
width(1)

penup()
home()
setheading(270)
forward(80/5)
setheading(0)
forward(-50)
# -55.00,-80.00
pendown()
color("black")
fillcolor("slate grey")

begin_fill()
setheading(230)
circle(200/5, 55)

setheading(28)
circle(270/5, 25)

print(pos())
#(47,-78)
penup()
goto(47, -78)
pendown()
setheading(-230)
circle(200, -57)
#circle(200, -48)
#print(pos())
#dot(10)

setheading(-30)
circle(270, -50)

end_fill()
penup()
goto(47, -78)
begin_fill()
pendown()
setheading(-230)
circle(200, -57)
setheading(-30)
circle(270, -50)
goto(47, -78)
end_fill()

penup()
home()
setheading(270)
forward(80)
pendown()
setheading(0)
forward(45)
forward(-90)

width(4)
#sword
penup()
goto(-55.00,-80.00)
pendown()
fillcolor("gray")
begin_fill()
setheading(225)
forward(15)
setheading(135)
forward(50)
setheading(225)
forward(20)
setheading(135)
forward(-50)
setheading(225)
forward(25)
setheading(315)
forward(20)
goto(-55.00,-80.00)
end_fill()

##penup()
##goto(91.84,-234.39)
##
##pendown()
##setheading(315)
##forward(30)
##setheading(160)
##forward(34)

penup()
goto(-1.10,-184.42) #home minus 184 for y coord
setheading(270)
forward(110)
setheading(0)
forward(20)
dot(20)
pendown()

##fillcolor("black")
##begin_fill()

setheading(270)
forward(8)
setheading(55)
circle(170, 23)
setheading(180)

penup()
forward(75)
setheading(270)
forward(57)
dot(20)

pendown()
setheading(270)
forward(8)
setheading(-55)
circle(170, -23)
penup()
setheading(0)
forward(35)
setheading(270)
forward(50)
pendown()

#end_fill()

setheading(90)
forward(40)
setheading(270)
circle(10, -90)
##setheading(0)
##forward(20)
penup()
setheading(270)
forward(60)
setheading(0)
forward(23)
pendown()
setheading(90)
forward(50)
setheading(-270)
circle(10, 90)
setheading(180)
forward(10)






#exit gracefully
hideturtle()
done()
