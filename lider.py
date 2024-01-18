def find_majority(arr):
    counter = 0
    candidate = 0

    for e in arr:
        if counter == 0:
            candidate = e
            counter = 1
        elif e == candidate:
            counter += 1
        else:
            counter -= 1

    if arr.count(candidate) >= len(arr) / 2:
        return candidate
    else:
        return -1


l = [1, 2, 5, 5, 7, 5, 5, 10, 5, 5]
print(l, "\n", find_majority(l))
