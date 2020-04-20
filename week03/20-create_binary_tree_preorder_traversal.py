# Return the root node of a binary search tree that matches the given preorder traversal.

# (Recall that a binary search tree is a binary tree where for every node, any descendant of node.left has a value < node.val, and any descendant of node.right has a value > node.val.  Also recall that a preorder traversal displays the value of the node first, then traverses node.left, then traverses node.right.)


# Example 1:

# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]


# Note:

# 1 <= preorder.length <= 100
# The values of preorder are distinct.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def bstFromPreorder(preorder):
    if len(preorder) == 0:
        return None

    def insert(curr, value):
        if value < curr.val:
            if curr.left is None:
                curr.left = TreeNode(value)
            else:
                insert(curr.left, value)
        elif value > curr.val:
            if curr.right is None:
                curr.right = TreeNode(value)
            else:
                insert(curr.right, value)

    node = TreeNode(preorder[0])

    for i in range(1, len(preorder)):
        insert(node, preorder[i])

    return node
