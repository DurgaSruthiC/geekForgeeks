a=[]
n=int(input())
for i in range(n):
    a.append(input("Enter val"))
print(a)
for i in range(len(a)):
    poped_ele=a.pop()
    print('poped ele is',poped_ele)