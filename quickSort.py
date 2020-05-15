def quickSort(arr,low,high):
    if low<high:
        pivot = arr[high-1]
        a = b = low
        for i in range(low,high):
            if arr[i]<=pivot:
                temp = arr[a]
                arr[a] = arr[b]
                arr[b] = temp
                a+=1
                b+=1
            elif arr[i]>pivot:
                b = b + 1

        quickSort(arr,low,a-1)
        quickSort(arr,a,high)



#Driver code
#import random
print("Enter the size of array")
n = int(input())
arr = []
print("Enter the elements of array")
for i in range(n):
    arr.append(int(input()))
    #arr.append(random.randint(1,1000)*10)
quickSort(arr,0,len(arr))
print(arr)

