from turtle import *


def drawSquare(x, y):
	pendown()
	for i in range(2):
		forward(x)
		right(90)
		forward(y)
		right(90)
	penup()


# Set turtle color and background color
bgcolor("black")
color("brown")

penup()
goto(-25, -10)
left(90)

# Draw Cross
begin_fill()
drawSquare(250, 50)
end_fill()

goto(-125, 200)
right(90)

begin_fill()
drawSquare(250, 40)
end_fill()

# Draw Text under the cross
goto(0, -130)
color("white")
write("God's Got You!", font=("Arial", 30, "normal"), align="center")

hideturtle()
done()
