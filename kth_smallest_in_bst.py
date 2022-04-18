# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.count = 0
        self.kth = 0
        
    def inorder(self, root, k):
        if root and self.count < k:
            self.inorder(root.left, k)
            pass # visit root
            print('Value=',root.val)
            self.count = self.count + 1
            if(self.count == k):
                self.kth = root.val
                return root.val
            self.inorder(root.right, k)
            
    
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.inorder(root,k)
        return self.kth
        
