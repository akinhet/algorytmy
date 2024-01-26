# https://mattomatti.com/pl/a0048
def functionzero(f, a, b, e=0.0001):
    fa = f(a)
    if fa == 0:
        return fa
    fb = f(b)
    if fb == 0:
        return fb

    if fa * fb > 0:
        return

    c = (a+b)/2
    fc = f(c)
    while (abs(fc) > e):
        if fc * fa > 0:
            a = c
            fa = fc
        else:
            b = c
            fb = fc
        c = (a+b)/2
        fc = f(c)

    return c


def func(x):
    return x**3 + x**2 - 1


print(functionzero(func, 0, 2))
print(functionzero(func, 0, 2, 0.0000001))
print(functionzero(func, 0, 2, 0.01))
