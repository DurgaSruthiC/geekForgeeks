#https://practice.geeksforgeeks.org/problems/occurences-of-2-as-a-digit/1
#Occurences of 2 as a digit
#Count the number of 2s as digit in all numbers from 0 to n.
#Input:
#The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains the input integer n.
#Output:
#Print the count of the number of 2s as digit in all numbers from 0 to n.
#Constraints:
#1<=T<=100
#1<=N<=10^5
#Example:
#Input:
#2
#22
#100
#Output:
#6
#20

def numberOf2sinRange(n):
    a=[]
    for i in range(1,n+1):
        a.append(i)
    st=''
    for i in a:
        st+=str(i)
    ab=[]
    for i in st:
        ab.append(int(i))
    return ab.count(2)