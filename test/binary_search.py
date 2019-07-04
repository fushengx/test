def binary_search(array, target):

    low = 0
    high = len(array)-1
    while low <= high:
        mid = int((low+high) / 2)
        guess = array[mid]
        if guess == target:
            return mid
        if guess > target:
            high = mid - 1
        else:
            low = mid + 1
    return None



array = [1, 2, 5, 6, 33, 57, 99]
B = binary_search(array, 6)
print(B)
