from turtle import Turtle
from turtle import Screen

def star():
    
    turtle = Turtle()
    screen = Screen()
    screen.colormode(255)

    turtle.hideturtle()
    turtle.penup()
    turtle.setposition((20, 61))
    turtle.begin_fill()
    turtle.pendown()
    turtle.color((255, 215, 0), (255, 215, 0))
    turtle.forward(10)
    for i in range(9):      
      if i%2==1:            
        turtle.left(72)
      else:            
        turtle.right(144)
      turtle.forward(10)
    turtle.penup()
    turtle.end_fill()