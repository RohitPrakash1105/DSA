class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, parent_node, child_data, is_left=True):
        # Create the child node
        child = Node(child_data)

        if self.root is None:
            self.root = parent_node  # Set the parent node as the root
            print(f"Root set to: {parent_node.data}")
        else:
            # Now directly add the child to the parent node
            if is_left:
                if parent_node.left is None:
                    parent_node.left = child
                else:
                    print(f"Left child already exists for {parent_node.data}")
            else:
                if parent_node.right is None:
                    parent_node.right = child
                else:
                    print(f"Right child already exists for {parent_node.data}")

    # Inorder traversal (for testing)
    def inorder_traversal(self, node):
        if node is not None:
            self.inorder_traversal(node.left)
            print(node.data, end=" ")
            self.inorder_traversal(node.right)

# Example usage:
tree = BinaryTree()

# Create nodes manually
root_node = Node("Root")
left_child = Node("Left Child")
right_child = Node("Right Child")

# Insert nodes without needing to find the parent by data
tree.insert(root_node, "Left Child", is_left=True)
tree.insert(root_node, "Right Child", is_left=False)
tree.insert(left_child, "Left Grandchild", is_left=True)
tree.inorder_traversal(tree.root)