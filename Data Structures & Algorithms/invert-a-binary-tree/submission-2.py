# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        BFS:
        left, right, = right, left
        pick next child, switch values
        '''
        if not root:
            return None
        if not root.left and not root.right:
            return root

        q = deque([root])
        while q:
            curr = q.popleft()
            if curr.left and curr.right:
                curr.left, curr.right = curr.right, curr.left
                q.append(curr.left)
                q.append(curr.right)
            elif curr.left:
                curr.left, curr.right = None, curr.left
                q.append(curr.right)
            elif curr.right:
                curr.left, curr.right = curr.right, None
                q.append(curr.left)
  
        return root

