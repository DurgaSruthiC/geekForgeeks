#Q: https://practice.geeksforgeeks.org/problems/kth-smallest-element/0
# 3rd smallest element in the given array is 7.
#Input:
#2   T
#6   N
#7 10 4 3 20 15   arr
#3
#5
#7 10 4 20 15
#4

#Output:
#7
#15

def kSmallEle(T):
    N=int(input())
    arr=list(map(int,input().split()))
    k=int(input())
    arr.sort()
    print(arr[k-1])
    return arr[k-1]
T=int(input())
for i in range(T):
    kSmallEle(T)