class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
            self.tail=self.head
        else:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
    def display(self):
        self.tail=self.head
        while self.tail:
            print(self.tail.data)
            self.tail=self.tail.next
    def pop(self):
        temp=self.head
        self.head=self.head.next
a=stack()
for i in range(int(input("Enter your range: "))):
    a.push(i)
a.display()


