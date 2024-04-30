class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class queue:
    def __init__(self) -> None:
        self.front=None
        self.rear=None
    def enqueue(self):
        newnode=Node(int(input("Enter the number: ")))
        if self.front==None:
            self.front=newnode
            self.rear=self.front
        else:
            self.rear.next=newnode
            self.rear=newnode
    def dequeue(self):
        temp=self.front
        self.front=self.front.next
        self.rear.next=self.front
    def peak(self):
        print("Peak Element is : ",self.front.data)
    def display(self):
        temp=self.front
        while temp.next != self.front:
            print(temp.data)
            temp=temp.next
        print(temp.data)
a=queue()
for i in range(int(input("enter your range:"))):
    a.enqueue()
a.dequeue()
a.peak()
a.display()
