def fastpowiter(x, n):
    ret = 1

    while n > 0:
        if n % 2 == 1:
            ret *= x

        x *= x
        n //= 2

    return ret


def fastpowrek(x, n):
    if n <= 0:
        return 1

    ret = fastpowrek(x, n // 2) ** 2

    if n % 2 == 1:
        ret *= x

    return ret


print(fastpowiter(2, 4))
print(fastpowrek(2, 4))
