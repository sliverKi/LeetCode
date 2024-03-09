# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #return : 앞에서 부터 k번째 <-> 뒤에서 k번째 swap
        temp = head
        stack=[]
        length = 0
        if not head: return 
        while temp:
            stack.append(temp)
            temp=temp.next
            length += 1
        
        start = stack[k-1]
        end = stack[length-k]
       
        start.val, end.val = end.val, start.val
        return head
        
       
        
        
        
        
        