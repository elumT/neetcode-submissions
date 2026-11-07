# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummy = ListNode()
        p3 = dummy
        while p1 and p2:
            if p1.val <= p2.val:
                p3.next = ListNode(val=p1.val)
                p1 = p1.next
            else:
                p3.next = ListNode(val=p2.val)
                p2 = p2.next
            p3 = p3.next
        while p1:
            p3.next = ListNode(val=p1.val)
            p1 = p1.next
            p3 = p3.next
        while p2:
            p3.next = ListNode(val=p2.val)
            p2 = p2.next
            p3 = p3.next
        return dummy.next
        