# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1=0
        num2=0
        tp = 1
        while l1:
            num1 = num1+tp*l1.val
            l1 = l1.next
            tp = tp*10
        tp = 1
        while l2:
            num2 = num2+tp*l2.val
            l2 =l2.next
            tp = tp*10
        res = num1+num2
        prev = ListNode(0)
        ret = prev
        while(res != 0):
            ret.next = ListNode((res%10))
            ret = ret.next
            res = res/10
        if prev.next:
            return prev.next
        else :        
            return ListNode(0)
