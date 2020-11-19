#Question link: https://practice.geeksforgeeks.org/problems/max-distance-between-same-elements/1
def maxDistance(arr, n):
    ab=list(set(arr))
    max_distn=[]
    for i in range(len(ab)):
        a=[]
        for j in range(len(arr)):
            if ab[i]==arr[j]:
                a.append(j)
        max_distn.append(max(a)-min(a))
    return (max(max_distn)) 

#output:
If input is [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2] then output is 10

arr[] = {3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2}
Max Distance 10
maximum distance for 2 is 11-1 = 10
maximum distance for 1 is 4-2 = 2
maximum distance for 4 is 10-5 = 5
Test case 1: 
arr[] = {1, 1, 2, 2, 2, 1}
Max Distance: 5
Distance for 1 is: 5-0 = 5
Distance for 2 is : 4-2 = 2
Max Distance 5