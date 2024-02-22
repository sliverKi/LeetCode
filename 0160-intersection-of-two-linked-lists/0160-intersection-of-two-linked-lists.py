# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        currA, currB = headA, headB
        lenA=0
        lenB=0
        
        while currA:
            lenA+=1
            currA=currA.next
        
        while currB:
            lenB+=1
            currB=currB.next
    
        if lenA > lenB:
            for _ in range(lenA-lenB):
                headA=headA.next    
        else:
            for _ in range(lenB-lenA):
                headB=headB.next
        
        tempA, tempB = headA, headB
        
        while headA:
            if tempA == tempB:
                return tempA
            tempA=tempA.next#pointer
            tempB=tempB.next#pointer
        return None



