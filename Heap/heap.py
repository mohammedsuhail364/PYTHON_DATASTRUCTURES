class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.right=None
        self.left=None
class Minheap:
    def __init__(self) -> None:
        self.root=None
    def add(self,data):
        if not self.root:
            self.root=Node(data)
            return
        self.recursiveadd(data,self.root)
    def recursiveadd(self,data,node):
        if not node.left:
            node.left=Node(data)
        elif not node.right:
            node.right=Node(data)
        else:
            if self.getcount(node.left)<=self.getcount(node.right):
                self.recursiveadd(data,node.left)
            else:
                self.recursiveadd(data,node.right)
    def getcount(self,node):
        if not node:
            return 0
        return 1+self.getcount(node.left)+self.getcount(node.right)
heap=Minheap()
heap.add(10)
heap.add(7)
heap.add(6)
heap.add(5)
heap.add(4)

        