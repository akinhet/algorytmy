import turtle


def treefractal(degree, length):
    turtle.forward(length)
    if degree > 0:
        turtle.left(45)
        treefractal(degree - 1, length / 2)
        turtle.right(90)
        treefractal(degree - 1, length / 2)
        turtle.left(45)
    turtle.back(length)


turtle.speed(0)
turtle.left(90)
treefractal(5, 200)
turtle.done()
