import random


def pibymontecarlo(N):
    trafione = 0
    for i in range(N):
        x = random.random() * 2 - 1
        y = random.random() * 2 - 1

        if x*x + y*y <= 1:
            trafione += 1

    return 4 * trafione / N


print(pibymontecarlo(100000))
