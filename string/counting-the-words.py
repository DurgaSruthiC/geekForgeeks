#https://practice.geeksforgeeks.org/problems/the-counting-game/0
T=int(input())
def sequenceOfWords(s):
    c=1
    capital=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    for i in range(len(s)):
        #if s[i].isupper():
        if s[i] in capital:
            c=c+1
    print(c)
for i in range(T):
    s=input()
    sequenceOfWords(s)
