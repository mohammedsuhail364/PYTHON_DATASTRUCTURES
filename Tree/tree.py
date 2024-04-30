class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]
class Tree:
    def __init__(self):
        self.root=None
    def add(self,data,parentnode=None):
        newnode=TreeNode(data)
        if self.root is None:
            self.root=newnode
            return
        parentnode=self.findnode(parentnode,self.root)
        if parentnode is None:
            print("Parent Not Found")
            return
        parentnode.children.append(newnode)
        
    def findnode(self,data,node):
        if node.data==data:
            return node
        for child in node.children:
            nodefound=self.findnode(data,child)
            if nodefound:
                return nodefound
        return None
    def display(self,depth=0,node=None):
        if node is None:
            node=self.root
        print(" "*depth,node.data)
        for child in node.children:
            self.display(depth+1,child)
    def remove(self,data):
        if not self.root:
            print("Tree is Empty")
            return
        if self.root.data==data:
            self.root=None
            return
        parentnode=self.findparentnode(data,self.root)
        if parentnode:
            for child in parentnode.children:
                if child.data==data:
                    parentnode.children.remove(child)
                    return
        print("Node Not Found")
    def findparentnode(self,data,node):
        for child in node.children:
            if child.data==data:
                return node
            nodefound=self.findparentnode(data,child)
            if nodefound:
                return nodefound
        return None
tree=Tree()
tree.add(1)
tree.add(2,1)
tree.add(3,1)
tree.add(4,2)
tree.add(5,2)
tree.add(6,3)
tree.add(7,3)
tree.add('a',1)
tree.display()
print("-----------------")
tree.remove('a')
tree.display()
    




