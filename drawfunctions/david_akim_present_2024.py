from turtle import Turtle


def draw_present():
    turtle = Turtle()
    turtle.hideturtle()

    # Draw box
    turtle.penup()
    turtle.goto(60, 0)
    turtle.pendown()
    turtle.color(2, 181, 91)
    turtle.begin_fill()
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.end_fill()

    # Draw box lid
    turtle.penup()
    turtle.goto(55, 0)
    turtle.pendown()
    turtle.color(0, 212, 105)
    turtle.begin_fill()
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(40)
    turtle.end_fill()

    # Draw ribbon
    turtle.penup()
    turtle.goto(78, -30)
    turtle.pendown()
    turtle.color(255, 0, 0)
    turtle.begin_fill()
    turtle.forward(6)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(6)
    turtle.right(90)
    turtle.forward(50)
    turtle.end_fill()

    # Draw right bow
    turtle.penup()
    turtle.goto(80, 12)
    turtle.pendown()
    bow_rad = 12
    turtle.width(5)
    for i in range(2):
        # two arcs
        turtle.circle(bow_rad, -90)
        turtle.circle(bow_rad//4, -90)

    # Draw left bow
    turtle.penup()
    turtle.goto(55, 22)
    turtle.pendown()
    for i in range(2):
        # two arcs
        turtle.circle(bow_rad, 90)
        turtle.circle(bow_rad//4, 90)
