# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        linked = []
        while head is not None:
            linked.append(head.val)
            head = head.next
        linked = linked[::-1]

        result = 0
        for i in range(len(linked)):
            num = linked[i] * pow(2, i) 
            result += num

        return result

        