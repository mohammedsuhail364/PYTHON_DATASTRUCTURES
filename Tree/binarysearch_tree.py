class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    def search(self, root, key):
        if root is None or root.val == key:
            print("True")
            return root
        else:
            print("False")
        if root.val < key:
            return self.search(root.right, key)
        return self.search(root.left, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val, end=" ")
            self.inorder_traversal(root.right)

    def find_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def delete_node(self, root, key):
        if root is None:
            return root

        if key < root.val:
            root.left = self.delete_node(root.left, key)
        elif key > root.val:
            root.right = self.delete_node(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.find_min_value_node(root.right)
            root.val = temp.val
            root.right = self.delete_node(root.right, temp.val)
        return root

# Example usage:
bst = BST()
root = None
keys = [50,30,70,20,40,60,80,65]
for key in keys:
    root=bst.insert(root, key)

print("Inorder Traversal:")
bst.inorder_traversal(root)
print("\n")

# Deleting nodes
delete_keys = [50]
for key in delete_keys:
    print(f"Deleting node with key: {key}")
    root = bst.delete_node(root, key)
    print("Inorder Traversal after deletion:")
    bst.inorder_traversal(root)
    print("\n")
# bst.search(root,10)
