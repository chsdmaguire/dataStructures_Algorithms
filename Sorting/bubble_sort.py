# sorts array of integers using bubble sort algorithm


array1 = [8, 5, 2, 9, 5, 6, 3]

# BEST: O(n) time | O(1) space
# AVERAGE: O(n^2) time | O(1) space
# WORST: O(n^2) time | O(1) space


def bubble_sort(arr):
    sorted = False
    counter = 0
    while not sorted:
        sorted = True
        for i in range(len(arr) - 1 - counter):
            if arr[i] > arr[i + 1]:
                swap(i, i + 1, arr)
                sorted = False
        counter += 1
    return arr


def swap(i, j, arr):
    arr[i], arr[j] = arr[j], arr[i]


print(bubble_sort(array1))
