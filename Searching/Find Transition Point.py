#You are given a sorted array containing only numbers 0 and 1. Find the transition point efficiently. Transition point is a point where "0" ends and "1" begins.
#Example:

#Input
#1
#5
#0 0 0 1 1

#Output
#3
def transitionPoint(arr, n):
    for i in range(len(arr)):
        if arr[i]==1:
            return i
            break