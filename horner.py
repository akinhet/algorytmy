def horner(W, x):
    ret = 0

    for i in range(len(W) - 1, -1, -1):
        ret = ret * x + W[i]

    return ret


W = [2, 3, 5, 1]
print(horner(W, 2))
W = [1]
print(horner(W, 2))
