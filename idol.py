def find_idol(arr):
    for i in range(len(arr)):
        if arr[i] == [0] * len(arr):
            for j in range(len(arr)):
                if i == j:
                    continue
                elif arr[j][i] == 0:
                    break
            else:
                return i
    return -1


m = [
    [0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 0, 0]
]

print(find_idol(m))
