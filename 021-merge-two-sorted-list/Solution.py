


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prevhead = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                prevhead.next = l1
                l1 = l1.next
            else:
                prevhead.next = l2
                l2 = l2.next

        prevhead = l1 if l1 is not None else l2

        return dummy.next
