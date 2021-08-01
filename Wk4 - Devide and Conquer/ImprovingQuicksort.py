right= int(input("Input the last index of up comming list  "))

sequence = [int(index) for index in input("Enter sequence ").split()]

#Random pivot
import random
from turtledemo.sorting_animate import partition


def quickSort(arr, left, right) :
    # print('Splitting: ', arr[left:right])
    if left + 1>= right:
        return
    # Select the pivor randomly
    pivot = random.randint(left, right - 1)

    arr[left], arr[pivot] = arr[pivot], arr[left]

    #Patition array
    pivot1, pivot2,= partition(arr, left, right)

    #Recursively call quicksort
    quickSort(arr, left, pivot1)
    quickSort(arr, pivot2 + 1, right)


def partition(arr, left, right) :
    pivot2 = left
    for i in range(left + 1, right):
        if arr[i] <= arr[left]:
            arr[pivot2 + 1], arr[i] = arr[i], arr[pivot2 +1]
            pivot2 +=1

    arr[left], arr[pivot2] = arr[pivot2], arr[left]
    pivot1 = left

    for i in range(left, pivot2) :
        if arr[i] < arr[pivot2]:
            arr[i], arr[pivot1] = arr[pivot1], arr[i]
            pivot1 +=1
    return pivot1, pivot2

quickSort(sequence, 0, right)
#Print output
print(' '.join([str(i) for i in sequence]))
