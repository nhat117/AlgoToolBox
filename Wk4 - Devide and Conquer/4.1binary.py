# Enter input sequence:
sequence = [int(index) for index in input().split()]

search_sequence = [int(index) for index in input().split()]
num = sequence[0]
sequence = sequence[1:]


# Binary search_sequence
def binarysearch(seque, key, right):
    left = 0
    while left <= right:
        middle = (left + right) // 2
        if key > seque[middle]:
            left = middle + 1
        elif key < seque[middle]:
            right = middle - 1
        else:
            return middle
    # If not appeare in the sequence
    return -1

#Driver code
solution = list()
for i in search_sequence[1:]:
    answer = binarysearch(sequence, i, num - 1)
    solution.append(answer)
print(' '.join([str(i) for i in solution]))
