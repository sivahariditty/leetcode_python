#Intersection of Two Linked Lists
#Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A,B = headA,headB
        na = 0
        nb = 0
        while A:
            A = A.next
            na = na+1
        while B:
            B = B.next
            nb = nb+1
        lg = nb
        lr = headB
        lm = headA
        diff = nb - na
        if na > nb:
            lg = na
            lr = headA
            lm = headB
            diff = na - nb
        A,B = headA,headB
        for i in range(diff):
            lr = lr.next
        for j in range(lg - diff):
            if(lr == lm):
                return lr
            if lr.next:
                lr = lr.next
            if lm.next:
                lm = lm.next
        return None

