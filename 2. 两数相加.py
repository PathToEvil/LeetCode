# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1 = l1
        p2 = l2
        total = 0
        head = ListNode(0)
        end = head
        while p1 or p2:
            total //= 10
            if p1:
                total += p1.val
                p1 = p1.next
            if p2:
                total += p2.val
                p2 = p2.next
            end.next = ListNode(total % 10)
            end = end.next
        if total > 10:
            end.next = ListNode(total // 10)
        return head.next