def bubbleSort(arr):
    n = len(arr)

    for num in range(n - 1):
        for j in range(0, n - num - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

list = [5,2,8,1,3,6,9,0,4]
bubbleSort(list)

print(f"Bubble sort: {list}")

#------------------------------------------------------------------------------

def selection_sort(array):
    for i in range(0, len(array) - 1):
        smallest = i
        for j in range(i + 1, len(array)):
            if array[j] < array[smallest]:
                smallest = j
        array[i], array[smallest] = array[smallest], array[i]

list2 = [5,2,8,1,3,6,9,0,4]
selection_sort(list2)

print(f"selection sort: {list2}")