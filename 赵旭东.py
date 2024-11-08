import turtle
turtle.colormode(255)
turtle.color(127,0,64)
turtle.fillcolor(255,235,179)
turtle.begin_fill()
count=0
while count < 6:
	turtle.forward(100)
	turtle.right(360/6)
	count +=1
turtle.end_fill()
turtle.done()
