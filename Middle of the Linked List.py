# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        first_p = head
        second_p = head

        while second_p and second_p.next:
            first_p = first_p.next
            second_p = second_p.next.next
        
        return first_p
