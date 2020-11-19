str1="adcffaet"
patt="onkl"
str1="laacbjfedrkwollbhfqfvkvpndxetrvetvgvenb"
patt="jflhvzuwgconxaionnnugfpky"
https://practice.geeksforgeeks.org/problems/minimum-indexed-character/0

str1="vsizcnmjilegtiugfxqtkeggknxxojrlczmgozrykxgefdmkadfmjotvdsuremfgnroeqfeddljkqvvqacejszfwszpwnue"
patt="douhezn"
#str1="geeks"
#patt="set"
#p=str1.split('').join(',')
#print(p)
c=0
a=[]
#comparing each ele in 2 arrays and then storing the matched str1 index in array
#sort the array and return min index value of array
T=int(input())
def min_index(str1,patt):
    temp=0
    for i in range(len(str1)):
        for j in range(len(patt)):
            if str1[i] == patt[j]:
                temp=str1[i]
        if temp!=0:
            break
    if temp!=0:
        print(temp)
    else:
        print('$')
for i in range(T):
    str=input()
    patt=input()
    min_index(str,patt)