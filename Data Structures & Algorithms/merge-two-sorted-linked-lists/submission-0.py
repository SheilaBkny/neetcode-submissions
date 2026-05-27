# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        when one is None, return the other. 
        keep going. until 
        
        '''

        if not list1 and not list2:
            return None
        elif not list1:
            return list2
        elif not list2:
            return list1


        node = ListNode(0, None)

        curr = node

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = ListNode(list1.val, None)
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = ListNode(list2.val, None)
                curr = curr.next
                list2 = list2.next

        if not list1:
            curr.next = list2
        else:
            curr.next = list1

        return node.next
            
            















