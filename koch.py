import turtle


def kochcurve(degree, length):
    if degree > 0:
        kochcurve(degree - 1, length / 3)
        turtle.left(60)
        kochcurve(degree - 1, length / 3)
        turtle.right(120)
        kochcurve(degree - 1, length / 3)
        turtle.left(60)
        kochcurve(degree - 1, length / 3)
    else:
        turtle.forward(length)


def kochsnowflake(degree, length):
    kochcurve(degree, length)
    turtle.right(120)
    kochcurve(degree, length)
    turtle.right(120)
    kochcurve(degree, length)
    turtle.right(120)


turtle.speed(0)
kochsnowflake(5, 300)
turtle.done()
