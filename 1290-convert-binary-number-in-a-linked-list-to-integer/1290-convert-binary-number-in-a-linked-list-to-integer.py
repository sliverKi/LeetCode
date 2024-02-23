# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # 링크드리스트의 값들을 빈리스트를 만들어 추가시켜주었다.
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

        