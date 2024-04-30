class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def create(self):
        temp=node(int(input("enter your number: ")))
        if self.head==None:
            self.temp=temp
            self.head=temp
        else:
            self.temp.next=temp
            self.temp=self.temp.next
    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
        print('')
    def insertion(self,position):
        count=1
        self.temp=self.head
        while True:
            if position==1:
                tempobj=node(int(input("enter the insertion number: ")))
                tempobj.next=self.temp
                self.head=tempobj
                break
            elif position==count:
                if self.temp.next==None:
                     tempobj=node(int(input("enter the insertion number: ")))
                     self.temp.next=tempobj
                     break
                else:
                    tempobj=node(int(input("enter the insertion number: ")))
                    tempobj.next=self.temp
                    self.pre.next=tempobj
                    break
            else:
                count+=1
                self.pre=self.temp
                self.temp=self.temp.next
    def deletion(self,pos):
        count=1
        self.temp=self.head
        while True:
            if pos==1:
                self.head=self.temp.next
                break
            elif pos==count:
                self.pre.next=self.temp.next
                break
            else:
                count+=1
                self.pre=self.temp
                self.temp=self.temp.next
    def reverse(self):
        self.temp = None
        temp1 = self.head.next
        while self.head:
            self.head.next = self.temp
            self.temp = self.head
            if temp1:
                self.head = temp1
                temp1 = temp1.next
            else:
                break
        self.head = self.temp

    

a=linkedlist()
for i in range(int(input("enter your range: "))):
    a.create()
a.display()
a.insertion(int(input("enter the position: ")))
a.display()
a.deletion(int(input("enter the deleting position: ")))
a.display()
a.reverse()
a.display()

