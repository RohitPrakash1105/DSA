class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
class BinarySearchTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        new_node = Node(data)

        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        parent_node = None

        while current_node is not None:
            parent_node = current_node

            if data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right

        if data < parent_node.data:
            parent_node.left = new_node
        else:
            parent_node.right = new_node
    def inorder_traversal(self,node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data,end=" ")
            self.inorder_traversal(node.right)
    def preorder_traversal(self, node):
        if node is not None:
            print(node.data, end=" ")
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)
    def postorder_traversal(self, node):
        if node is not None:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.data, end=" ")

my_tree = BinarySearchTree()
for i in [ 46,25,5,100,1000,2000,250,500,40,80,45]:
    my_tree.insert(i)
my_tree.inorder_traversal(my_tree.root)
my_tree.preorder_traversal(my_tree.root)