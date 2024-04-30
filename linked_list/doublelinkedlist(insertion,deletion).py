class Node:
   def __init__(self, data):
      self.data = data
      self.next = None
      self.prev = None
class doubly_linked_list:
    def __init__(self):
       self.head = None
    def create(self):
        newnode=Node(int(input("Enter your number: ")))
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
    def insertion(self,position):
          self.temp=self.head
          count=1
          while True:
             if position==1:
                insertno=Node(int(input("Enter the insert number: ")))
                insertno.next=self.temp
                self.head=insertno
                self.head.pre=None
                break
             elif position==count:
                if self.temp.next==None:
                   insertno=Node(int(input("Enter the insert number: ")))
                   self.temp.next=insertno
                   insertno.prev=self.temp
                   break
                else:
                  insertno=Node(int(input("Enter the insert number: ")))
                  insertno.pre=self.pre
                  insertno.next=self.temp
                  self.pre.next=insertno
                  self.temp.pre=insertno
                  break
             else:
                self.pre=self.temp
                self.temp=self.temp.next
                count+=1
    def deletion(self,pos):
       count=1
       self.temp=self.head
       while True:
          if pos==1:
             self.head=self.temp.next
             self.head.pre=None
             print(self.head.pre)
             break
          elif pos==count:
             if self.temp.next==None:
                self.pre.next=self.temp.next
                break
             else:
                self.pre.next=self.temp.next
                self.temp=self.temp.next
                self.temp.pre=self.pre
                break
          else:
             count+=1
             self.pre=self.temp
             self.temp=self.temp.next
a=doubly_linked_list()
for i in range(int(input("Enter your range: "))):
    a.create()
a.display()
a.insertion(int(input("Enter the insert position: ")))
a.display()
a.deletion(int(input("Enter the deleting number position: ")))
a.display()
   
