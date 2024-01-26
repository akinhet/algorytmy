def distribute(n):
    i = 2

    ret = []

    while n > 1:
        if n % i == 0:
            ret.append(i)
            n //= i
        else:
            i += 1

    return ret


print(distribute(15))
print(distribute(60))
print(distribute(7))
