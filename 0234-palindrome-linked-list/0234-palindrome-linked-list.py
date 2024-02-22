# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
    
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # print(slow, fast)
        
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        # print(prev)
        
        left, right = head, prev
        while right: 
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

  
       