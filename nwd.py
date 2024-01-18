# wersja iteracyjna
def nwd_iter(a, b):
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a


def nwd_rek(a, b):
    if b > 0:
        return nwd_rek(b, a % b)
    return a


print("nwd(50, 10) = 10")
print("iter", nwd_iter(50, 10))
print("rek", nwd_rek(50, 10))

print("\nnwd(5012, 10) = 2")
print("iter", nwd_iter(5012, 10))
print("rek", nwd_rek(5012, 10))

print("\nnwd(12, 160) = 4")
print("iter", nwd_iter(12, 160))
print("rek", nwd_rek(12, 160))
