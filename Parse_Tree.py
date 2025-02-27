from Nodes_And_References import BinaryTree
import operator

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

class Stack:
    """Stack implementation as a list"""

    def __init__(self):
        """Create new stack"""
        self._items = []

    def is_empty(self):
        """Check if the stack is empty"""
        return not bool(self._items)

    def push(self, item):
        """Add an item to the stack"""
        self._items.append(item)

    def pop(self):
        """Remove an item from the stack"""
        return self._items.pop()

    def peek(self):
        """Get the value of the top item in the stack"""
        return self._items[-1]

    def size(self):
        """Get the number of items in the stack"""
        return len(self._items)
     
def build_parse_tree(fp_expr: str):
    fp_list = fp_expr.split()
    p_stack = Stack()
    expr_tree = BinaryTree("")
    p_stack.push(expr_tree)
    current_tree = expr_tree

    for i in fp_list:
        if i == "(":
            current_tree.insert_left("")
            p_stack.push(current_tree)
            current_tree = current_tree.left_child
        elif i in ["+", "-", "*", "/"]:
            current_tree.root = i
            current_tree.insert_right("")
            p_stack.push(current_tree)
            current_tree = current_tree.right_child
        elif i.isdigit():
            current_tree.root = int(i)
            parent = p_stack.pop()
            current_tree = parent
        elif i == ")":
            current_tree = p_stack.pop()
        else:
            raise ValueError(f"Unknown operator '{i}")

    return expr_tree

def evaluate(parse_tree):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul, 
        "/": operator.truediv
    }

    left_child = parse_tree.left_child
    right_child = parse_tree.right_child

    if left_child and right_child:
        fn = operators[parse_tree.root]
        return fn(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree.root

def to_list(tree):
    """Convert the binary tree to a list of lists representation."""
    if tree is None:
        return []
    
    result = [tree.root]
    left_child = to_list(tree.left_child)
    right_child = to_list(tree.right_child)
    
    if left_child or right_child:
        result.append(left_child)
        result.append(right_child)
    
    return result

def to_expr(tree_list):
    """converts the list expression of the binary tree back to an infix expression."""
    if isinstance(tree_list, int):
        return str(tree_list)
    
    # Assuming tree_list is a list with three elements: [operator, left_subtree, right_subtree]
    operator = tree_list[0]
    left = to_expr(tree_list[1])
    right = to_expr(tree_list[2])

    return f"( {left} {operator} {right} )" 

# Example usage
pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))

# Visualize as list of lists
parse_tree_as_list = to_list(pt)
print(parse_tree_as_list)

# Example usage
parse_tree_as_list = [ '*', [ '+', 10, 5 ], 3 ]
expression = to_expr(parse_tree_as_list)
print(expression)