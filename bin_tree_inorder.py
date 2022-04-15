# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.ret = []
    
    def inOrder(self, root):
        if root:
            self.inOrder(root.left)
            self.ret.append(root.val)
            self.inOrder(root.right)
        else:
            return
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.ret = []
        self.inOrder(root)
        return self.ret
