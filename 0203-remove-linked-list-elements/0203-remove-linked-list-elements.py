# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        temp = ListNode(next=head)#{val: 0, next:{1,2,6,3,4,5,6}}
        current = temp
        
        if not head:
            return head

        while current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return temp.next

       