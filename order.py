def sort(array):
    for i in range(len(array)-1):
        for j in range(len(array) -i -1):
            if array[j] > array[j +1]:
                array[j], array[j +1] = array[j +1], array[j]

array = [5, 99, 2, 1, 33, 57, 6]

sort(array)
print(array)
