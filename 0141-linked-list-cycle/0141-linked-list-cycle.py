# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        first = head
        second = head
        
        while first!= None and first.next!=None:
            first = first.next.next
            second = second.next
            if first == second:
                return True
        return False
        
        
        