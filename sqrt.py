def sqrtheron(n, e=0.0001):
    x1 = n / 2
    x2 = (x1 + (n / x1)) / 2

    while abs(x2 - x1) > e:
        x1 = (x2 + (n / x2)) / 2
        x1, x2 = x2, x1

    return x2


def sqrtnewton(n, e=0.0001):
    x = n / 2

    while abs(x - n / x) > e:
        x = (x + n / x) / 2

    return x


print(sqrtheron(2))
print(sqrtnewton(2))
