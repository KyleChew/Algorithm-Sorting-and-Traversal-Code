def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [10,9,7,8,4,5,1,3,12,18,17,16,15,14,11,19,15,20,6,2,13]
bubbleSort(alist)
print(alist)

