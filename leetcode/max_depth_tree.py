# maximum depth of a binary tree
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None 
        self.right = None 

class Solution:
    def maxDepth(self, root):
        """
        type root: TreeNode
        rtype: int
        """
        if root is None:
            return 0
        else:
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
            
        