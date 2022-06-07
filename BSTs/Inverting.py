

def invert_binary_tree(tree):
    if tree is None:
        return
    tree.left, tree.right = tree.right, tree.left
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
