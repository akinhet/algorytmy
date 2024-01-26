def minmax(T):
    N = len(T)
    if N == 1:
        return T[0], T[0]

    min = []
    max = []
    i = 0
    while i + 1 < N:
        if T[i] < T[i+1]:
            min.append(T[i])
            max.append(T[i+1])
        else:
            min.append(T[i+1])
            max.append(T[i])
        i += 2

    if i < N:
        min.append(T[i])
        max.append(T[i])

    mini = min[0]
    maxi = max[0]
    for j in range(1, round(N/2)):
        if mini > min[j]:
            mini = min[j]
        if maxi < max[j]:
            maxi = max[j]

    return mini, maxi


A = [6, 3, 1, 9, 2]
B = [6, 3, 1, 9, 2, 4]
print(minmax(A))
print(minmax(B))
