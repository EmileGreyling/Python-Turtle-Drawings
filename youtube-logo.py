"""
   *********************************************************************************
   *                    Program to draw the YouTube Logo                           * 
   *********************************************************************************
"""

# The turtle module provides a drawing board like feature, which enables us to create pictures and shapes.

from turtle import *

# Set the background color
bgcolor('black')

penup()
goto(-140, -100)
pendown()

# Set the color of the turtle
color('red')
begin_fill()

# Loop to draw red box
for i in range(2):
    forward(300)
    circle(10, 90)
    forward(200)
    circle(10, 90)

end_fill()

penup()
goto(-15, -30)
pendown()

# Set the color of the turtle
color('white')

# Loop to draw play button
begin_fill()
for i in [30, 120, 120]:
    left(i)
    forward(100)
end_fill()
hideturtle()

done()
