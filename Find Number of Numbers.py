#Q:https://practice.geeksforgeeks.org/problems/find-number-of-numbers/1/
def num(arr, n, k):
    # Code here
    s=''
    for i in arr:
        s+=str(i)   
    array_with_single_digit_ele=[]
    for i in s:
        array_with_single_digit_ele.append(int(i))
    return array_with_single_digit_ele.count(k)

Input:
arr=[11, 12, 13, 14, 15]
k=1
output:5 
Explntn:
arr is converted to a string  -->s
each char in string is converted to int and appended to arr.
count the occurence of ele in array using 'ar.count(no)'
