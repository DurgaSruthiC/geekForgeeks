#arr=[1,2,3,4,5]
#arr=[0, -10, 1, 3, -20]
#arr=[37, 6, -7, 41, -23, 15, 9, -14, -18, 1, -13, -22, 25, -43, 24 ]
#arr=[8, 45, -21, -13, -15, 43, -32, -22, -7, -39, -22, -21, 26, -46, -7, 13, -37, -12, -44, -10, -46, -32]
#postv -- >0 
def missingNumber(arr,n):
    arr=sorted(arr)
    c=0
    for i in range(1,max(arr)):
	#to chck all postv nos frm 1 to largest no.If any no is not found it wll be displayed
        if i not in arr:
            return i    
            break
	#if all the eles till the large no are present then it will disply the nxt no aftr big no.
	#c checks for all the nos present in the arr in the loop over arr
        if i in arr:
            c=c+1
            if c==len(arr)-1:
                return arr[i]+1
                break