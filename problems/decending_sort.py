class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sl:
    def __init__(self):
        self.head=None
        self.time=0
    def create(self,x):
        self.time+=1
        newnode=node(x)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=self.temp.next
    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next
    def sorting(self):
        self.temp=self.head
        self.pre=self.temp
        while self.pre!=None:
            self.temp=self.pre.next
            while self.temp!=None:
                if self.pre.data<self.temp.data:
                    self.pre.data,self.temp.data=self.temp.data,self.pre.data
                self.temp=self.temp.next
            self.pre=self.pre.next             
a=sl()
li=[1,2,3,4,5]
for i in li:
    a.create(i)
a.sorting()
a.display()