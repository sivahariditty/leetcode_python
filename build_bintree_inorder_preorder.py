# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.hsh = {}
        
    def splitBuild(self,preorder,left_i,right_i):
        if(left_i>right_i):
            return None
        x = preorder.pop(0)
        root = TreeNode(x)
        indx = self.hsh[x]
        root.left = self.splitBuild(preorder,left_i,indx-1)
        root.right = self.splitBuild(preorder,indx+1,right_i)
        return root
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        count = len(preorder)
        self.hsh = {num:i for i,num in enumerate(inorder)}
        return self.splitBuild(preorder,0,count-1)
