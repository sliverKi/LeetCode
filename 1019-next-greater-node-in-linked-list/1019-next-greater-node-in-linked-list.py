# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        node = head
        temp, stack = [], []
        while node:
            temp.append(node.val)
            node = node.next
        ans = [0]*len(temp)
        
        for idx, num in enumerate(temp):#KEY
            while stack and temp[stack[-1]] < num:
                ans[stack.pop()]=num
            stack.append(idx)#stack[0,1,2]
        return ans
            
        
        
                