from turtle import Turtle, Screen

def draw_shape():

  turtle = Turtle()
  screen = Screen()
  screen.colormode(255)

  turtle.hideturtle()
  turtle.penup()
  turtle.setposition((-150,-50))
  turtle.begin_fill()
  turtle.pendown()
  turtle.color((0, 0, 0), (0, 0, 0))
  turtle.speed(10)
  turtle.pensize(5)
  turtle.pencolor('#bf9900')

  for i in range(4):
    turtle.forward(100)
    turtle.left(90)

  for i in range(36):
    turtle.circle(50)
    turtle.left(10)

  turtle.end_fill()
