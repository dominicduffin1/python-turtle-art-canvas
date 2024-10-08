from turtle import Turtle


def draw_christmas_sock():
    turtle = Turtle()
    turtle.hideturtle()

    # top sock part
    turtle.up()
    turtle.goto(125, 50)
    turtle.down()
    turtle.rt(-25)
    turtle.fd(40)
    turtle.circle(-5, 90)
    turtle.fd(15)
    turtle.circle(-5, 90)
    turtle.fd(40)
    turtle.circle(-5, 90)
    turtle.fd(15)
    turtle.circle(-5, 90)
    turtle.up()
    # bottom sock part
    turtle.goto(171, 42)
    turtle.begin_fill()
    turtle.down()
    turtle.color('red')
    turtle.rt(90)
    turtle.fd(50)
    turtle.circle(-10, 90)
    turtle.fd(50)
    turtle.circle(-15, 180)
    turtle.fd(15)
    turtle.circle(10, 90)
    turtle.fd(20)
    turtle.rt(90)
    turtle.fd(35)
    turtle.end_fill()
