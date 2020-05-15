def insertionSort(arr):
    n = len(arr)
    for i in range(1,n):
        key = i
        for j in range(i-1,-1,-1):
            if arr[key]<arr[j]:
                temp = arr[key]
                arr[key] = arr[j]
                arr[j] = temp
                key = j

#DRIVER CODE
#import random
n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))
    #arr.append(random.randint(1,1000)*10)

insertionSort(arr)
print(arr)
