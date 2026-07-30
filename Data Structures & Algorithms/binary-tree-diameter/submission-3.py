# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # we need to return height(left) + height(right)
        # but theres a max somewhere that we need to get. 
        self.diameter = 0
        def height(root):
            if not root:
                return 0
            leftH = height(root.left)
            rightH = height(root.right)

            self.diameter = max(self.diameter, leftH + rightH)
            return 1 + max(leftH, rightH)

        height(root)
        return self.diameter

            

    
