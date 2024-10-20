from turtle import Turtle


def draw_candycane():
    turtle = Turtle()
    # turtle.speed(3)
    turtle.hideturtle()

    # candy cane
    turtle.up()
    turtle.goto(100, 90)
    turtle.down()
    turtle.rt(-90)
    turtle.circle(15, 180)
    turtle.fd(50)
    turtle.circle(5, 180)
    turtle.fd(50)
    turtle.circle(-5, 180)
    turtle.circle(5, 180)
    turtle.up()

    # red stripe
    turtle.goto(70, 70)
    turtle.down()
    turtle.begin_fill()
    turtle.color('red')
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(14)
    turtle.rt(135)
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(14)
    turtle.end_fill()

    # green stripe
    turtle.up()
    turtle.goto(70, 55)
    turtle.down()
    turtle.rt(135)
    turtle.begin_fill()
    turtle.color('green')
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(14)
    turtle.rt(135)
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(14)
    turtle.end_fill()

    # red stripe
    turtle.up()
    turtle.goto(70, 40)
    turtle.down()
    turtle.rt(135)
    turtle.begin_fill()
    turtle.color('red')
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(14)
    turtle.rt(135)
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(14)
    turtle.end_fill()

    # red stripe
    turtle.up()
    turtle.goto(90, 90)
    turtle.down()
    turtle.rt(135)
    turtle.begin_fill()
    turtle.color('red')
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(9)
    turtle.rt(135)
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(9)
    turtle.end_fill()

    # green stripe
    turtle.up()
    turtle.goto(70, 83)
    turtle.down()
    turtle.rt(135)
    turtle.begin_fill()
    turtle.color('green')
    turtle.fd(5)
    turtle.rt(45)
    turtle.fd(22)
    turtle.rt(50)
    turtle.fd(5)
    # turtle.rt(130)
    # turtle.fd(22)
    turtle.end_fill()
