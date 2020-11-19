#In this we will input values line by line
#2
#5
#2 2 1 7 5
#5
#2 2 3 5 6
def check_divisiblty(n):
    count=0
    for i in range(len(n)):
        for j in range(i):
            if(((n[i]+n[j])%4)==0):
                count=count+1
    print(count)        
    
T=int(input())
len_ar=range(T)
a=list(range(T))
print(len(len_ar))
for i in range(T):
    size=input()
    for j in range(len(size)):
        a[i]=list(map(int,input().split()))
for i in range(len(a)):
    check_divisiblty(a[i])

