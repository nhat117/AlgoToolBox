right= int(input("Input the last index of up comming list  "))

sequence = [int(index) for index in input("Enter sequence ").split()]

def devide_function(seqq, left, right) :
    if left + 1 == right :
        return  seqq[left]
    elif left + 2 == right :
        return  seqq[left]
    #Devide the element of the sequence
    middle = (left + right) //2
    left_seqq = devide_function(seqq, left, middle)
    right_seqq = devide_function(seqq, middle, right)

    ele1, ele2 = 0, 0
    for i in seqq[left: right] :
        if i == left_seqq:
            ele1 +=1
        elif i == right_seqq:
            ele2 += 1
    if ele1 > (right - 1) //2 and left != -1:
        return left
    elif ele2 > (right -1) //2 and right != -1:
        return right
    else:
        return -1


print(int(devide_function(sequence, 0, right) != -1))