# Windows Start Logo In Python

from turtle import *

# set the turtle's speed and width
speed(1)
width(4)

# Set background color
bgcolor('black')

# set color to blue
color('blue')

begin_fill()

penup()


goto(-50, 60)
pendown()

# Draw square
coordinates = [
		[100, 100],
		[100, -100],
		[-50, -60],
		[-50, 60]
	]

for x, y in coordinates:
	goto(x, y)

end_fill()


penup()

# Set the turtle's pen color to black
color('black')

# Change width of the turtle
width(10)


# Split shape into 4

goto(-50, 0)
pendown()

goto(100, 0)

penup()

goto(25, -80)
pendown()

goto(25, 80)
hideturtle()

done()
