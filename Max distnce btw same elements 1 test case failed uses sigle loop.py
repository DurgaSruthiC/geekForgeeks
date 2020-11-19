#arr=[13, 2, 1, 2, 1, 4, 15, 8, 9, 7, 4, 2, 3, 6, 2]
#Find max_distnce btw same elements in an array the flg is 1 loop soln
#It failed for array [1] where the output should be 1
def  max_Distance(arr):
    max_dis=0
    for i in arr:
        #print(i,arr.index(i))
        a=arr.index(i)
        b=len(arr)-arr[::-1].index(i)-1
        print(a,b)
        c=b-a
        if c>max_dis:
            print(c)
            return c
max_Distance(arr)