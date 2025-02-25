from Nodes_And_References import BinaryTree

def preorder(tree: BinaryTree):
    """preorder traversal"""
    if tree:
        print(tree.key)
        preorder(tree.get_left_child())
        preorder(tree.get_right_child())

def postorder(tree: BinaryTree):
    """""" 
    if tree:
        postorder(tree.get_left_child())
        postorder(tree.get_right_child())
        print(tree.key)

if __name__ == "__main__":
    a_tree = BinaryTree("a")
    # print(a_tree.get_root_val())
    # print(a_tree.get_left_child())
    a_tree.insert_left("b")
    # print(a_tree.get_left_child())
    # print(a_tree.get_left_child().get_root_val())
    a_tree.insert_right("c")
    # print(a_tree.get_right_child())
    # print(a_tree.get_right_child().get_root_val())
    a_tree.get_right_child().set_root_val("hello")
    # print(a_tree.get_right_child().get_root_val())

    preorder(a_tree)