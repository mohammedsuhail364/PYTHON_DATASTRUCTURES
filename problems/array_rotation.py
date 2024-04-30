class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def loop(self):
        self.temp=self.head
        while self.temp.next:
            self.pre=self.temp
            self.temp = self.temp.next
    def create(self,x):
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
    def rotate(self):
        self.temp=self.head
        while self.temp.next:
            self.temp=self.temp.next
        self.pre=self.head.next
        self.temp.next=self.head
        self.head.next=None
        self.head=self.pre
    def arrayrotate(self,x):
        self.temp=self.head
        while self.temp.next:
            self.pre=self.temp
            self.temp = self.temp.next
        for x in range(x):
            print(self.temp.data)
            self.temp = self.pre
            self.temp.next = None
            self.loop()
a=linkedlist()
li=[1,2,3,4,5]
for i in li:
    a.create(i)
a.display()
print("-----------------------------------")
for i in range(2):
    a.rotate()
a.display()
print("-----------------------------------")
a.arrayrotate(x=2)
a.display()

