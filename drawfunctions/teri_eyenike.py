from turtle import Turtle, Screen

def draw_shape():
  turtle = Turtle()
  Screen().setup(1.0, 1.0)
  Screen().bgcolor('black')

  turtle.shape('circle')
  turtle.speed(10)
  turtle.pensize(5)
  turtle.pencolor('magenta')

  for i in range(4):
    turtle.forward(100)
    turtle.left(90)

  for i in range(36):
    turtle.circle(50)
    turtle.left(10)

  turtle.hideturtle()
