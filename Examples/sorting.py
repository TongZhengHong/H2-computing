import random

def swap(array, first, second):
    temp = array[first]
    array[first] = array[second]
    array[second] = temp
    return array

def selection_sort(array):
    for track in range(len(array) - 1):
        low = array[track]
        low_index = track

        for i in range(track + 1, len(array)):
            if array[i] < low:
                low = array[i]
                low_index = i
        
        swap(array, low_index, track)
        print(array)

    return array

def bubble_sort(array):
    pointer = None

    while pointer != 0:
        pointer = 0

        for i in range(1, len(array)):
            if array[i - 1] > array[i]:
                swap(array, i, i - 1)
                pointer += 1

        print(array)

    return array

def insertion_sort(array):
    for i in range(1, len(array)):
        
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                swap(array, j, j - 1)
        print(array)

    return array

def main():
    array = []
    
    for i in range(10):
        array.append(random.randint(1, 100))

    print(array)
    print()

    array = insertion_sort(array)

    print()
    print(array)

main()