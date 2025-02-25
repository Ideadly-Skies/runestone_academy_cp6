class BinaryTree:
    def __init__(self, root_obj):
        """initialize a binary tree"""
        self.key = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        """insert new_node as left child of the binary tree"""
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.left_child = self.left_child
            self.left_child = new_child

    def insert_right(self, new_node):
        """insert new_node as right child of the binary tree"""
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            new_child = BinaryTree(new_node)
            new_child.right_child = self.right_child

    def get_root_val(self):
        """get the root of this binary tree"""
        return self.key
    
    def set_root_val(self, new_obj):
        """set the new root value with new_obj"""
        self.key = new_obj

    def get_left_child(self):
        """get the left children of the binary tree"""
        return self.left_child
    
    def get_right_child(self):
        """return the right child of the binary tree"""
        return self.right_child
    
    def __repr__(self):
        """return the key object of the binary tree"""
        return self.key

    def tree_exercise(self):
        """implement a tree that looks like the following"""
        a_tree = BinaryTree("a")
        a_tree.insert_left("b")
        a_tree.get_left_child().insert_right("d")
        a_tree.insert_right("c")
        a_tree.get_right_child().insert_left("e")
        a_tree.get_right_child().insert_right("f")
        return a_tree

if __name__ == "__main__":
    a_tree = BinaryTree("a")
    print(a_tree.get_root_val())
    print(a_tree.get_left_child())
    a_tree.insert_left("b")
    print(a_tree.get_left_child())
    print(a_tree.get_left_child().get_root_val())
    a_tree.insert_right("c")
    print(a_tree.get_right_child())
    print(a_tree.get_right_child().get_root_val())
    a_tree.get_right_child().set_root_val("hello")
    print(a_tree.get_right_child().get_root_val())