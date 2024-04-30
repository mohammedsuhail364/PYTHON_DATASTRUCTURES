class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
class doubly_linked_list:
    def __init__(self):
       self.head = None
    def create(self,x):
        newnode=Node(x)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            newnode.pre=self.temp
            self.temp=self.temp.next
    def display(self):
        self.temp=self.head
        while self.temp:
            print(self.temp.data)
            self.temp=self.temp.next
    def traverse(self,find):
        self.temp=self.head
        self.pre=self.temp
        while self.pre!=None:
            self.temp=self.pre.next
            while self.temp!=None:
                if self.pre.data+self.temp.data==find:
                    print(self.pre.data,self.temp.data)
                self.temp=self.temp.next
            self.pre=self.pre.next
a=doubly_linked_list()
li=[1,2,3,4,5,6]
for i in li:
    a.create(i)
a.traverse(find=6)