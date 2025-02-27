# add to the python path at runtime to import binary trees
import sys
import operator
sys.path.insert(1, "/Users/obie/Desktop/Jobs/Shopee/SeaLabs/DSA/runestone_academy_cp6")
from Nodes_And_References import BinaryTree

# traversal methods
def preorder(tree: BinaryTree):
    """
    we visit the root node first, then recursively do a preorder 
    traversal to the left subtree, followed by a recursive preorder
    traversal of the right subtree
    
    example: the book is the root of the tree, and each chapter is
    a child of the root. Each section within a chapter is a child of
    the chapter, each subsection is a child of its section, and so on.
    """
    if tree: # base case is to check whether the tree exists
        print(tree.key)
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree: BinaryTree):
    """
    we do a recursive postorder traversal of the left subtree and the right
    subtree followed by a visit to the root node 
    """ 
    if tree: # base case: check whether tree exists
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.key)

def inorder(tree: BinaryTree):
    """
    we do a recursive inorder traversal of the left subtree, the root, and then a 
    recursive inorder traversal of the right subtree 
    """
    if tree:
        inorder(tree.left_child)
        print(tree.key)
        inorder(tree.right_child)

def print_exp(tree: BinaryTree):
    result = ""
    if tree:
        result = "(" + print_exp(tree.left_child)
        result = result + str(tree.key)
        result = result + print_exp(tree.right_child) + ")"
    return result


def postordereval(tree: BinaryTree):
    """
    evaluate the parse tree 
    """

    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    result_1 = None
    result_2 = None

    if tree:
        result_1 = postordereval(tree.left_child)
        result_2 = postordereval(tree.right_child)
        if result_1 and result_2:
            return operators[tree.key](result_1, result_2) # add two results together
        return tree.key

if __name__ == "__main__":
    """instantiate instance of binary tree in here"""
    a_tree = BinaryTree("a")
    a_tree.insert_left("b")
    a_tree.get_left_child().insert_left("d")
    a_tree.insert_right("c")
    preorder(a_tree) # a, b, d, c

    b_tree = BinaryTree("/")
    b_tree.insert_left(4)
    b_tree.insert_right(4)
    
    print(postordereval(b_tree))