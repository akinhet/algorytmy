import turtle


def cantor(degree, length):
    if degree > 0:
        cantor(degree - 1, length / 3)
        turtle.penup()
        turtle.forward(length / 3)
        turtle.pendown()
        cantor(degree - 1, length / 3)
    else:
        turtle.forward(length)


turtle.speed(0)
turtle.back(250)
for i in range(6):
    cantor(i, 500)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.back(500)
    turtle.pendown()

turtle.done()
