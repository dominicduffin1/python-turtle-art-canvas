from turtle import Turtle
from turtle import Screen

def draw_snowman():

	turtle = Turtle()
	screen = Screen()

	turtle.hideturtle()
	turtle.penup()
	turtle.setposition((180, -10))
	turtle.pendown()
	turtle.color(("lightblue"), ("azure"))
	turtle.begin_fill()
	turtle.circle(26)
	turtle.penup()
	turtle.setposition((180, 42))
	turtle.pendown()
	turtle.circle(13)
	turtle.penup()
	turtle.setposition((180, 68))
	turtle.pendown()
	turtle.circle(8)
	turtle.end_fill()
	turtle.penup()
	#draw face and buttons
	turtle.setposition((178, 75))
	turtle.pendown()
	turtle.dot(2, "blue")
	turtle.penup()
	turtle.setposition((184, 75))
	turtle.pendown()
	turtle.dot(2, "blue")
	turtle.penup()
	turtle.setposition((180, 72))
	turtle.pendown()
	turtle.dot(3, "orange")
	turtle.penup()
	turtle.setposition((180, 50))
	turtle.pendown()
	turtle.dot(4, "black")
	turtle.penup()
	turtle.setposition((180, 60))
	turtle.pendown()
	turtle.dot(4, "black")
	turtle.penup()
	turtle.setposition((180, 30))
	turtle.pendown()
	turtle.dot(6, "black")
	turtle.penup()
	turtle.setposition((180, 20))
	turtle.pendown()
	turtle.dot(6, "black")
	turtle.penup()
	turtle.setposition((180, 10))
	turtle.pendown()
	turtle.dot(6, "black")

	#Draw hat

	turtle.penup()
	turtle.setposition((176, 80))
	turtle.pendown()
	turtle.color("gray")
	turtle.begin_fill()
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(8)
	turtle.left(90)
	turtle.forward(10)
	turtle.left(90)
	turtle.forward(8)
	turtle.end_fill()






