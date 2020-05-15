class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def listprint(self):
        printval=self.head
        while printval is not None:
            print(printval.data,'-->',end='')
            printval=printval.next
    def atbegin(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    def atend(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=newnode
    def atmiddle(self,middle,data):
        newnode=node(data)
        if middle is None:
            print('not found')
            return                  #1->2->3->4
        newnode.next=middle.next
        middle.next=newnode
    def remove(self,key):
        cur = self.head
        if cur and cur.data == key:
            self.head=cur.next
            cur=None
            return
        prev = None
        while cur and cur.data != key:
            prev=cur
            cur=cur.next
        if cur is None:
            return
        prev.next=cur.next
        cur=None
        
            
s1=Sll()
s1.head = Node('MON')
e2=Node('tue')
e3=Node('wed')
s1.head.next=e2
e2.next=e3
s1.atbegin('sun')
s1.atend('sat')
s1.atmiddle(e3,'thurs')
s1.remove('sun')
s1.listprint()

