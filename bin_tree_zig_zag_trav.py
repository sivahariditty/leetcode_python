# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Binary Tree Zigzag Level Order Traversal
# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[20,9],[15,7]]
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return None
        queue = []
        flg = True
        res = []
        ans = []
        queue.append(root)
        while queue:
            count = len(queue)
            for i in range(count):
                x = queue.pop(0)
                if flg:
                    res.append(x.val)
                else:
                    res.insert(0,x.val)
                if x.left is not None:
                    queue.append(x.left)
                if x.right is not None:
                    queue.append(x.right)
            flg = not flg
            ans.append(res)
            res = []
        return ans
