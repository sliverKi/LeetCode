# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#시간복잡도(time):O(m+n)
#공간복잡도(space):O(1)
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(None)#temp: pointer 초기화 
        node = temp#node == pointer
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next=list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return temp.next
        