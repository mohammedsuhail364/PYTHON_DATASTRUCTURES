#binarysearch tree and print inorder Traversal and pre_order traversal and post order traversal
class Node:
    def __init__(self,data):
        self.left=None
        self.data=data
        self.right=None
        
class tree:
    def __init__(self):
        self.root=None
    def add(self,data):
        if not self.root:#if self.root == None:
            self.root=Node(data)
        else:
            self.recursiveadd(data,self.root) 
    def recursiveadd(self,data,node):
        if data < node.data:
            if not node.left:
                node.left=Node(data)
            else:
                self.recursiveadd(data,node.left)
        elif data > node.data:
            if not node.right:
                node.right=Node(data)
            else:
                self.recursiveadd(data,node.right)
    def display(self):
        # result=[]
        # print("inorder_traversal")
        # self.inordertraversal(self.root,result)
        # print(result)
        # result=[]
        # print("preorder_traversal")
        # self.preordertraversal(self.root,result)
        # print(result)
        # result=[]
        # print("postorder_traversal")
        # self.postordertraversal(self.root,result)
        # print(result)
        result=[]
        self.inordertraversal(self.root,result)
        print(result)
    def inordertraversal(self,node,result):
        if not node:
            return None
        else:
            self.inordertraversal(node.left,result)
            result.append(node.data)
            self.inordertraversal(node.right,result)
    def preordertraversal(self,node,result):
        if not node:
            return None
        else:
            result.append(node.data)
            self.preordertraversal(node.left,result)
            self.preordertraversal(node.right,result)
    def postordertraversal(self,node,result):
        if not node:
            return None
        else:
            self.postordertraversal(node.left,result)
            self.postordertraversal(node.right,result)
            result.append(node.data)
    # def remove(self,data):
    #     if self.root==None:
    #         print("Tree is empty")
    #         return
    #     if self.root.data==data:
    #         self.root=None
    #         return 
    #     self.recursiveremove(self.root,data)
    def deletenode(self,key,root):
        if root==None:
            return root
        if key<root.data:
            root.left=self.deletenode(root.left,key)
        elif key > root.data:
            root.right=self.deletenode(root.right,key)
        else:
            if root.left==None:
                temp=root.right
                root=None
                return temp
            elif root.right==None:
                temp=root.left
                root=None
                return temp
            temp=self.find_min_value_node(root.right)
            root.data=temp.data
            root.right=self.deletenode(root.right,temp.data)
        return root
    def find_min_value_node(self,node):
        current=node
        while current.left:
            current=current.left
        return current
    
    # def recursiveremove(self,node,data):
    #     if node.left and data==node.left.data:
    #         node.left=None
    #         return
    #     elif node.right and node.right.data==data:
    #         node.right=None
    #         return
    #     elif data<node.data:
    #         self.recursiveremove(node.left,data)
    #     elif data>node.data:
    #         self.recursiveremove(node.right,data)
    def search(self,data):
        node=self.recursivesearch(self.root,data)
        if node:
            print("True")
        else:
            print("False")
    def recursivesearch(self,node,data):
        if not node:
            return node
        if node and node.data==data:
            return node
        elif data < node.data:
            return self.recursivesearch(node.left,data)
        elif data > node.data:
            return self.recursivesearch(node.right,data)

bst=tree()
bst.add(45)
bst.add(10)
bst.add(50)
bst.add(9)
bst.add(11)
bst.add(46)
bst.add(51)
bst.deletenode(key=10)
bst.display()
# bst.search(100)
# bst.display()