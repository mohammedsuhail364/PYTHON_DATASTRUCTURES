class Node:
    def _init_(self,data):
        self.data = data
        self.next = None
class QueueLinked:
    def _init_(self):
        self.head = None
    def create(self):
        n = int(input('To Insert In 1st Position Enter 1 Or To Insert In Last Position Enter 2: '))
        if n == 1:
            if self.head == None:
                newNode = Node(int(input("Enter The Element: ")))
                self.head = newNode
                self.temp = newNode
                self.tail = newNode
            else:
                newNode = Node(data=int(input("Enter The Element: ")))
                newNode.next = self.head
                self.head = newNode
        elif n == 2:
            if self.head == None:
                newNode = Node(int(input("Enter The Element: ")))
                self.head = newNode
                self.temp = newNode
                self.tail = newNode
            else:
                newNode = Node(int(input("Enter The Element: ")))
                self.temp.next = newNode
                self.temp = self.temp.next
                self.tail = newNode
    def dequeue(self):
        if self.head == None:
            print('UnderFLow')
        else:
            n = int(input('To Delete In 1st Position Enter 1 Or To Delete In Last Position Enter 2: '))
            if n == 1:
                self.head = self.head.next
            elif n == 2:
                self.temp = self.head
                while self.temp.next != None:
                    self.pre = self.temp
                    self.temp = self.temp.next
                self.pre.next = None
    def display(self):
        self.temp = self.head
        while self.temp:
            print(self.temp.data)
            self.temp = self.temp.next
a = QueueLinked()
a.create()
a.create()
a.create()
a.dequeue()
a.display()