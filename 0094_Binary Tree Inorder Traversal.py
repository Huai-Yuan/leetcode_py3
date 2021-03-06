# Anser on APP stil don't get it...
# Need to figure out what is TreeNode
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack, result = [], []
        while root:
            stack.append(root)
            root = root.left
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
                    
        return result