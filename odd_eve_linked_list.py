#Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

#The first node is considered odd, and the second node is even, and so on.

#Note that the relative order inside both the even and odd groups should remain as it was in the input.

#You must solve the problem in O(1) extra space complexity and O(n) time complexity.
#Input: head = [1,2,3,4,5]
#Output: [1,3,5,2,4]

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        odd = head
        eve = head.next
        evehd = eve
        while eve and eve.next:
            odd.next = odd.next.next
            eve.next = eve.next.next
            odd = odd.next
            eve = eve.next
        odd.next = evehd
        return head

