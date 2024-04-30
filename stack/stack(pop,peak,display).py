class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class stack:
    def __init__(self):
        self.head=None
        self.tail=None
    def push(self,data):
        newnode=Node(int(input("Enter the number: ")))
        if self.head is None:
            self.head=newnode
            self.tail=self.head
        else:
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
    def peak(self):
        print("Peak element is: ",self.head.data)
    
a=stack()
for i in range(int(input("Enter your range: "))):
    a.push(i)
a.pop()
a.peak()
a.display()


