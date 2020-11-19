#https://practice.geeksforgeeks.org/problems/equilibrium-point/0/
#Equilibrium point
#Input:
#The first line of input contains an integer T, denoting the number of test cases. Then T test cases follow. First line of each test case contains an integer N denoting the size of the array. Then in the next line are N space separated values of the array A.

#Output:
#For each test case in a new  line print the position at which the elements are at equilibrium if no equilibrium point exists print -1.

#Constraints:
#1 <= T <= 100
#1 <= N <= 106
#1 <= Ai <= 108

#Example:
#Input:
#2
#1
#1
#5
#1 3 5 2 2

#Output:
#1
#3


def equilibrium(A):
    c=0
    for i in range(len(A)):
        if sum(A[i+1:])-sum(A[:i])==0:
            c=i+1
    if c>1 or len(A)==1:
        print(c)
    else:
        print("-1")
T=int(input())
for i in range(T):
    #N=int(input())
    A=list(map(int,input().split()))
    equilibrium(A)
