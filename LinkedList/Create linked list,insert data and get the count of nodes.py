class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    #Print fn to display the elements in linked list    
    def printlist(self):
        temp=self.head
        while(temp):
            print(temp.data)
            temp=temp.next
    def countlist(self):
        temp=self.head
        c=0
        while(temp):
            temp=temp.next
            c=c+1 
        print(c)
if __name__=='__main__':
    llist=LinkedList()
    llist.head=Node('a')
    second=Node('b')
    third=Node('a')
    llist.head.next = second
    second.next = third
    llist.printlist() #prints list
    llist.countlist()#prints count of nodes