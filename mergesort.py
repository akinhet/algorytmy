def mergesort(A):
    if len(A) == 1:
        return A

    middle = len(A) // 2

    A1 = mergesort(A[:middle])
    A2 = mergesort(A[middle:])

    ret = []
    a1 = a2 = 0
    for i in range(len(A1) + len(A2)):
        if a1 >= len(A1) or (a2 < len(A2) and A1[a1] > A2[a2]):
            ret.append(A2[a2])
            a2 += 1
        elif a2 >= len(A2) or (a1 < len(A1) and A1[a1] <= A2[a2]):
            ret.append(A1[a1])
            a1 += 1

    return ret


A = [6, 3, 1, 9, 2]
print(mergesort(A))
