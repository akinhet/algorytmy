def binarysearch_iter(arr, searched):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (right + left) // 2
        if arr[mid] > searched:
            right = mid - 1
        elif arr[mid] < searched:
            left = mid + 1
        else:
            return mid

    return -1


def binarysearch_rek(arr, searched, left, right):
    mid = (right + left) // 2

    if left > right:
        return -1
    if arr[mid] == searched:
        return mid
    elif arr[mid] > searched:
        return binarysearch_rek(arr, searched, left, mid - 1)
    else:
        return binarysearch_rek(arr, searched, mid + 1, right)


array = [3, 4, 5, 6, 8, 8, 9]
x = 3

print(binarysearch_iter(array, x))
print(binarysearch_rek(array, x, 0, len(array)-1))
