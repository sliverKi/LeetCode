# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        left=[]
        right=[]
        #stack에 value만 넣음
        while temp:
            left.append(temp.val)
            temp = temp.next
        #스택의 맨 첫번째와 맨 마지막 요소를 각각 pop()한다. -> 스택을 나눠서 나중에 합치자 
        for i in range(len(left)//2):#i: 0,1까지
            right.append(left.pop())
        
        temp = head#재선언 
        for el1, el2 in zip_longest(left, right):#서로 길이가 달라 zip_longest()사용함, 길이가 동일할때는 zip()
            if el1:
                temp.val=el1
                temp=temp.next
            if el2:
                temp.val = el2
                temp=temp.next
        return head
        

        
        
