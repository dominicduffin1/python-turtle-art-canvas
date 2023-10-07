import turtle


def base():
    t = turtle.Turtle()
    t.color("brown")

    t.penup()
    t.goto(-2, -10)
    t.pendown()

    # Draw the tree base as a rectangle
    t.begin_fill()
    t.forward(40)   # Base width
    t.left(90)
    t.forward(20)   # Base height
    t.left(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.end_fill()
