"""110. Balanced Binary Tree
Easy
Topics
premium lock icon
Companies
Given a binary tree, determine if it is height-balanced.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: true
Example 2:


Input: root = [1,2,2,3,3,null,null,4,4]
Output: false
Example 3:

Input: root = []
Output: true
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-104 <= Node.val <= 104"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def check(node):
            if not node:
                return 0  # height of empty subtree is 0
            
            left = check(node.left)
            if left == -1:
                return -1  # left subtree is unbalanced
            
            right = check(node.right)
            if right == -1:
                return -1  # right subtree is unbalanced
            
            if abs(left - right) > 1:
                return -1  # current node is unbalanced
            
            return max(left, right) + 1  # return height of the subtree

        return check(root) != -1
