import math


def sito_remove(N):
    arr = []
    for i in range(2, N+1):
        arr.append(i)

    index = 0
    while index < math.sqrt(N):
        j = arr[index] * 2
        while j <= N:
            try:
                arr.remove(j)
            except:
                pass
            j += arr[index]
        index += 1

    return arr


def sito_zero(N):
    arr = [1] * N
    arr[0] = 0
    arr[1] = 0

    for i in range(int(math.sqrt(N)) + 1):
        if arr[i] == 0:
            continue

        j = i * 2

        while j < N:
            arr[j] = 0
            j += i

    return arr


print(sito_remove(30))
print(sito_zero(30))

for i, j in enumerate(sito_zero(30)):
    if j == 1:
        print(i, end=' ')

print()
