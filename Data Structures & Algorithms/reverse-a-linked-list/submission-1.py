# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        create a new linked list:
        fill in th linked list from the beginning, updating the head each time
        
        '''

        if not head:
            return None

        node = None
        curr = head
        while curr:
            newHead = ListNode(curr.val, node)
            node = newHead
            curr = curr.next

        return newHead