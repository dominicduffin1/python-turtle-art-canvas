from turtle import *

def draw_shape():
  shape('circle')
  setup(1.0, 1.0)
  bgcolor('black')
  speed(10)
  pensize(5)
  pencolor('magenta')

  for i in range(4):
    forward(100)
    left(90)

  for i in range(36):
    circle(50)
    left(10)

  hideturtle()

draw_shape()
