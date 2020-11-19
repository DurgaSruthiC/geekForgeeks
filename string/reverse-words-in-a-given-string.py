#https://practice.geeksforgeeks.org/problems/reverse-words-in-a-given-string/0

T=int(input())
def reverse_string(S):
    st=S.split('.')
    st1=""
    for i in range(len(st)-1,-1,-1):
        if i!=0:
            st1+=st[i]+'.'
        if i==0:
            st1+=st[i]
    print(st1)
    return st1

for i in range(T):
    S=input()
    reverse_string(S)




#----------------------------------
st="i.like.this.program.very.much"
s=st.split('.')
print(s)
st1=""
for i in range(len(s)-1,-1,-1):
    print(i,s[i])
    if i!=0:
        st1+=s[i]+'.'
    if i==0:
        st1+=s[i]
print(st1)