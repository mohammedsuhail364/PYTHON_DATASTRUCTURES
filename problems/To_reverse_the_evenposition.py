class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
        self.time=0
        self.lis=[]
    def create(self,x):
        self.time+=1
        temp=node(x)
        if self.head==None:
            self.temp=temp
            self.head=temp
        else:
            self.temp.next=temp
            self.temp=self.temp.next
    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next
    def even(self):
        self.temp=self.head
        if self.time>3:
            pos=0
            while self.temp.next:
                pos+=1
                self.pre=self.temp
                self.temp=self.temp.next
                if pos%2!=0:
                    self.lis.append(self.temp.data)
                    self.pre.next=self.temp.next
                    self.temp=self.pre
            self.insert()
        else:
            self.display()
    def insert(self):
        self.temp=self.head
        self.lis.reverse()
        for i in range(len(self.lis)):
            self.next1=self.temp.next
            newnode=node(self.lis[i])
            self.temp.next=newnode
            self.temp=self.temp.next
            self.temp.next=self.next1
            self.temp=self.temp.next
a=linkedlist()
li=[1,2,3,4,5,6]
for i in li:
    a.create(i)
a.even()
a.display()