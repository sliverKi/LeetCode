# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        cur = head
        dummy=[]
        length = 0
        
        
        while cur:
            length+=1
            cur = cur.next
        
        part, left = length//k, length%k
        cur = head
        prev = None
        
        for i in range(k):
            dummy.append(cur)
            for _ in range(part):
                if cur:
                    prev=cur
                    cur=cur.next
            if left and cur:
                prev=cur
                cur=cur.next
                left-=1
            if prev:
                prev.next=None
        return dummy