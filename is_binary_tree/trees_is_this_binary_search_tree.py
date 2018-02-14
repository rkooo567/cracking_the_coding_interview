""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    def checkBSTHelper(root, maximum, minimum):
        if root.left is None and root.right is None:
            return True
        elif not (root.data > root.left.data and root.data < root.right.data):
            return False
        elif not (root.right.data < maximum and root.left.data > minimum):
            return False
        else:        
            left = checkBSTHelper(root.left, root.data, minimum)
            right = checkBSTHelper(root.right, maximum, root.data)
            return left and right
    return checkBSTHelper(root, 9999999999999999999, -9999999999999999999999)
