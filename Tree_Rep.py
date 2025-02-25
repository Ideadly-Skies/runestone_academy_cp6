my_tree = [
        "a",        # root
            ["b",   # left subtree
                ["d", [], []],
                ["e", [], []] 
            ],
            ["c",   # right subtree
                ["f", [], []],
                []
            ], 
    ]

def make_binary_tree(root):
    """create the binary tree"""
    return [root, [], []]

def insert_left(root, new_child):
    """insert to the left of the binary tree"""
    old_child = root.pop(1) # pop index 1 which corresponds to the left subtree
    if len(old_child) > 1:
        root.insert(1, [new_child, old_child, []])
    else:
        root.insert(1, [new_child, [], []])
    return root

def insert_right(root, new_child):
    """insert right to the root"""
    old_child = root.pop(2) # pop index 2 which corresponds to the right subtree
    if len(old_child) > 1:
        root.insert(2, [new_child, [], old_child])
    else:
        root.insert(2, [new_child, [], []])
    return root

def get_root_value(root):
    """return root value of the tree""" 
    return root[0]

def set_root_val(root, new_value):
    """set root value of root"""
    root[0] = new_value

def get_left_child(root):
    """get left child of root"""
    return root[1]

def get_right_child(root):
    """get right child of root"""
    return root[2]

def tree_exercise():
    """write a function build_tree that returns a tree using the list of lists functions that looks like this""" 

    # create the root and left subtree 
    root = make_binary_tree("a")
    insert_left(root, "b")
    insert_right(get_left_child(root), "d")

    # create the root and right subtree
    insert_right(root, "c")
    insert_left(get_right_child(root), "e")
    insert_right(get_right_child(root), "f")

    # print root representation
    print(root) 

if __name__ == "__main__":
    tree_exercise()