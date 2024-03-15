# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #7243+0564 = 7807
        
        stack_l1, stack_l2 = [], []
        temp = 0
        head = None
        while l1:
            stack_l1.append(l1)
            l1=l1.next
        while l2:
            stack_l2.append(l2)
            l2=l2.next
        
        while stack_l1 or stack_l2:
            num1 = stack_l1.pop().val if stack_l1 else 0
            num2 = stack_l2.pop().val if stack_l2 else 0
            sum = num1+num2
            temp, sum = divmod(sum+temp, 10)
            node = head
            head = ListNode(sum)
            head.next = node
        if temp:
            node = head
            head = ListNode(temp)
            head.next = node
        return head



            
       



