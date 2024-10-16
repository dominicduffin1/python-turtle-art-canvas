from turtle import Turtle
from turtle import Screen

def tree_present():
    
    turtle = Turtle()
    screen = Screen()
    screen.colormode(255)

    turtle.hideturtle()
    turtle.penup()
    turtle.setposition((10, -5))
    turtle.right(90)

    # front of box
    turtle.pendown()
    turtle.begin_fill()
    turtle.color((219,112,147), (219,112,147))
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()
    turtle.end_fill()

    # move turtle to center of box for horizontal ribbon 
    turtle.color((75,0,130), (138,43,226))
    turtle.right(90)
    turtle.forward(8)

    # horizontal ribbon
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(20)
    turtle.penup()
    turtle.end_fill()

    # move turtle to top right corner of box
    turtle.left(90)
    turtle.forward(8)

    # vertical ribbon
    turtle.color((75,0,130), (138,43,226))
    turtle.left(90)
    turtle.forward(8)
    
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(4)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(4)
    turtle.penup()
    turtle.end_fill()

    # bow
    # right side of bow
    turtle.color((75,0,130), (138,43,226))
    turtle.begin_fill()
    turtle.left(25)

    turtle.pendown()
    turtle.forward(8)
    turtle.left(105)
    turtle.forward(8)
    turtle.left(120)
    turtle.forward(10)
    turtle.penup()
    turtle.end_fill()

    # left side of bow
    turtle.color((0,0,0), (138,43,226))
    turtle.begin_fill()
    turtle.right(60)
    turtle.forward(2)
    
    turtle.pendown()
    turtle.right(25)
    turtle.forward(10)
    turtle.right(120)
    turtle.forward(8)
    turtle.right(105)
    turtle.forward(8)
    turtle.penup()
    turtle.end_fill()
