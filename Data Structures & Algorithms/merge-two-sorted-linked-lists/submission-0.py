# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        curr = None
        l1Curr = list1
        l2Curr = list2
        while l1Curr or l2Curr:
            append = None
            if not l1Curr:
                append = l2Curr
                l2Curr = l2Curr.next
            elif not l2Curr:
                append = l1Curr
                l1Curr = l1Curr.next
            elif l1Curr.val < l2Curr.val:
                append = l1Curr
                l1Curr = l1Curr.next
            else:
                append = l2Curr
                l2Curr = l2Curr.next
            if not res:
                res = ListNode(append.val)
                curr = res
            else:
                curr.next = ListNode(append.val)
                curr = curr.next
        return res
            