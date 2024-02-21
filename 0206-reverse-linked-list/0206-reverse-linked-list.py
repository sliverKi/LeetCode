
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head == None or head.next == None:
            return head
           
        before = None
        temp = head
        
        while temp:
            after = temp.next  
            temp.next = before  
            before = temp  
            temp = after  
        return before  
