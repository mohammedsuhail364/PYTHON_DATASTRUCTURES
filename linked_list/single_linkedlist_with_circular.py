class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singlecircularlist:
    def __init__(self):
        self.head=None
        self.count=0
    def create(self):
        self.count+=1
        newnode=Node(int(input("Enter the number: ")))
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=self.temp.next
    def display(self):
        self.temp=self.head
        while self.temp.next != None:
            self.temp = self.temp.next
        self.temp.next = self.head
        self.temp = self.head
        for i in range(self.count):
                print(self.temp.data)
                self.temp=self.temp.next
    def insertion(self,position):
        self.temp=self.head
        count=1
        while True:
            if position==1:
                insertno=Node(int(input("Enter your insert number: ")))
                insertno.next=self.temp
                self.head=insertno
                self.count+=1
                break
            elif position==count:
                if self.temp.next==None:
                    insertno=Node(int(input("Enter your insert number: ")))
                    self.temp.next=insertno
                    self.count+=1
                    break
                else:
                    insertno=Node(int(input("Enter your insert number: ")))
                    self.pre.next=insertno
                    insertno.next=self.temp
                    self.count+=1
                    break
            else:
                count+=1
                self.pre=self.temp
                self.temp=self.temp.next
    def deletion(self,position):
        self.temp=self.head
        count=1
        while True:
            if position == 1:
                self.head=self.temp.next
                self.temp=self.temp.next
                self.count-=1
                for i in range(self.count-1):
                    self.temp=self.temp.next
                self.temp.next=None
                break
            elif position==count:
                if self.temp.next==self.head:
                    self.pre.next=None
                    self.count-=1
                    break
                else:
                    self.pre.next=self.temp.next
                    self.temp=self.head
                    self.count-=1
                    for i in range(self.count-1):
                        self.temp=self.temp.next
                    self.temp.next=None
                    break
            else:
                count+=1
                self.pre=self.temp
                self.temp=self.temp.next
a=Singlecircularlist()
for i in range(int(input("Enter the number range: "))):
    a.create()
# a.display()
a.insertion(int(input("Enter the insertion position: ")))
a.display()
a.deletion(int(input("Enter the deletion position: ")))
a.display()
