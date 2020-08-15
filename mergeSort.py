def mergeSort(arr, n):
    if n>1:                     # Divide the array in 2 parts until the length of array is 1
        arr1 = arr[:int(n/2)]
        arr2 = arr[int(n/2):]
        mergeSort(arr1,len(arr1))
        mergeSort(arr2,len(arr2))
        i=0
        k=0
        j=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr[k] = arr1[i]
                k+=1
                i+=1    
            elif arr2[j]<arr1[i]:
                arr[k] = arr2[j]
                k+=1
                j+=1
        while i<len(arr1):
            arr[k]=arr1[i]
            k+=1
            i+=1
        while j<len(arr2):
            arr[k]=arr2[j]
            j+=1
            k+=1

#DRIVER CODE
import random
n = int(input())
arr = []
for i in range(n):
    arr.append(random.randint(1,1000))
    #arr.append(int(input()))
mergeSort(arr,n)
print(arr)
