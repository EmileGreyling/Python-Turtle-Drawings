# Windows Start Logo In Python

# import turtle module
from turtle import *

# set the turtle's speed
speed(1)
width(4)

# Set background color
bgcolor('black')

# set color to blue
color('blue')

begin_fill()

penup()

# Move the turtle to the starting point
goto(-50, 60)
pendown()
# Move to right top
goto(100, 100)
# Move to right bottom
goto(100, -100)
# Move to left bottom
goto(-50, -60)
# Move back to starting point
goto(-50, 60)

end_fill()

penup()

# Set the turtle's pen color to black
color('black')

# Change width of the turtle
width(10)


# Cut shape into two halves

# Start at left middle
goto(-50, 0)
pendown()

# Go to  middle right
goto(100, 0)

penup()

# Cut shape into two halves verticaally
# Start from top
goto(25, -80)
pendown()
# Go to bottom
goto(25, 80)
hideturtle()

done()
