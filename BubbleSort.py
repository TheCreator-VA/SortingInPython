def BubbleSort(elements):
    n = len(elements)
    for i in range(n):
        for j in range(n-i-1):
            if elements[j]>elements[j+1]:
                 elements[j],elements[j+1] = elements[j+1],elements[j]



#DRIVER CODE
#import random
if __name__ =="__main__":
    n = int(input())
    arr=[]
    for i in range(n):
       #arr.append(random.randint(1,1000))
       arr.append(int(input()))
    BubbleSort(arr)
    print(arr)
    

