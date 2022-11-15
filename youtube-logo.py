"""
   *********************************************************************************
   *                    Program to draw the YouTube Logo                           * 
   *********************************************************************************
"""

# The turtle module provides a drawing board like feature, which enables us to create pictures and shapes.

import turtle as t
from time import sleep

t.penup()
t.goto(-140, -100)
t.pendown()

t.fillcolor('red')
t.begin_fill()

# Loop to draw red box
for i in range(2):
    t.forward(300)
    t.circle(10, 90)
    t.forward(200)
    t.circle(10, 90)

t.end_fill()

t.penup()
t.goto(-15, -30)
t.pendown()

# Loop to draw play button
t.fillcolor('white')
t.begin_fill()
for i in [30, 120, 120]:
    t.left(i)
    t.forward(100)
t.end_fill()
t.hideturtle()

# Write text below YouTube Logo
t.penup()
t.goto(-140, -150)
t.pendown()

t.write("Thanks For Watching!", move=True, font=("Verdana", 21, "normal"))
sleep(5)
