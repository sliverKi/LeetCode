# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy=ListNode(0)
        dummy.next=head
        node = dummy
        
        if not head.next or left==right:return head
        for _ in range(left-1):
            node = node.next
        
        reverse = node.next
        tail = reverse.next#swap
        
        # Reverse the sublist from left to right
        for _ in range(right - left):
            reverse.next = tail.next
            tail.next = node.next
            node.next = tail
            tail = reverse.next
            
        return dummy.next
        
        