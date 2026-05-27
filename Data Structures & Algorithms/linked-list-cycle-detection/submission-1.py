# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
       #using fast slow pointers. 

        slow = head
        fast = head

        #if the pointers meet at som epoint, then there is a cycle

       #we knoe there is no cycle when slow reaches the end

        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False

