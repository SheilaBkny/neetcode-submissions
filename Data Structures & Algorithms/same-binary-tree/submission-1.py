# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS on both trees, comparing each node

        q1 = deque([p])
        q2 = deque([q])

        if not p and not q:
            return True
        elif not p:
            return False
        elif not q:
            return False

        while q1 and q2:
            curr1 = q1.popleft()
            curr2 = q2.popleft()

            if curr1.val != curr2.val:
                return False
            
            if curr1.left and curr2.left:
                q1.append(curr1.left)
                q2.append(curr2.left)
            elif ((not curr1.left and curr2.left)
             or (not curr2.left and curr1.left)):
                return False
  
            if curr1.right and curr2.right:
                q1.append(curr1.right)
                q2.append(curr2.right)
            elif((not curr1.right and curr2.right)
             or (not curr2.right and curr1.right)):
                return False
        if len(q1) != len(q2):
            return False

        return True


            

        