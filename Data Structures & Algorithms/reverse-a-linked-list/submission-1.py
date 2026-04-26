# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode], prev = None) -> Optional[ListNode]:
        if not head:
            return head
        nextNode = head.next
        head.next = prev
        if not nextNode:
            return head
        return self.reverseList(nextNode, head)