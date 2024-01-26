import math


def distance(ax, ay, bx, by):
    return math.sqrt((ax - bx)**2 + (ay - by)**2)


def pointonsegment(px, py, ax, ay, bx, by):
    return distance(ax, ay, px, py) + distance(bx, by, px, py) == distance(ax, ay, bx, by)


print(pointonsegment(5, 5, 1, 1, 6, 6))
print(pointonsegment(5, 5, 1, 1, 4, 4))
print(pointonsegment(5, 4, 1, 1, 6, 6))
