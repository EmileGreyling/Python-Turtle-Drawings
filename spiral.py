from turtle import *
from itertools import cycle

colors = cycle(['red', 'orange', \
	'yellow', 'green', 'blue', 'purple'])

def draw_circle(size, angle, shift):
	color(next(colors))
	circle(size)
	right(angle)
	forward(shift)
	draw_circle(size + 2, angle + 2, \
		shift + .5)

hideturtle()
bgcolor('black')
speed(15)
pensize(4)
draw_circle(30, 0, 1)