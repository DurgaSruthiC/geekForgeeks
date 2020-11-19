#https://practice.geeksforgeeks.org/problems/linked-list-of-strings-forms-a-palindrome/1
#Given a linked list of strings having n nodes check to see whether the combined string formed is palindrome or not. 
#Example:
#Input :
#2
#5
#a bc d dcb a
#4
#a bc d ba

#Output :
#True
#False

#Explanation:
#case 1 : as String "abcddcba" is palindrome the function should return true
#case 2 : as String "abcdba" is not palindrome the function should return false

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def countlist(self):
        temp=self.head
        c=0
        str1=''
        while(temp):
            str1+=(temp.data)
            print(type(temp))
            temp=temp.next
            c=c+1 
        print(c)
        print(str1)
        if str1 == str1[::-1]:
            print('ok')
if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node('a')
    second=Node('b')
    third=Node('a')
    llist.head.next = second
    second.next = third
    llist.printlist()
    llist.countlist()