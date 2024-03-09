# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        temp = head
        while temp:
            if temp not in stack:#stack에 없으면 push
                stack.append(temp)
            else:#stack에 이미 있는 수인 경우
                if temp in stack:
                    # print("이미 있는 수의 인덱스", temp.val)
                    return temp
                break
            temp=temp.next
        return None
        
        #...Refactoring
        # while temp:
        #     if temp in stack:
        #         return temp
        #     stack.append(temp)
        #     temp = temp.next
        # return None