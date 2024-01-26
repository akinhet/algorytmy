import math


def pointlinedistance(px, py, a, b, c):
    up = abs(a * px + b * py + c)
    down = math.sqrt(a*a + b*b)

    return up / down


print(pointlinedistance(1, 1, 3, 2, 5))
