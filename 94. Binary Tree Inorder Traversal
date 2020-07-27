# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Given a binary tree, return the inorder traversal of its nodes' values.
# https://leetcode.com/problems/binary-tree-inorder-traversal/description/

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        result = []
        stack = [(1, root)]
        while stack:
            go_deeper, node = stack.pop()
            if node is None:
                continue
            if go_deeper:
                stack.append((1, node.right))
                stack.append((0, node))
                stack.append((1, node.left))
            else:
                result.append(node.val)
        return result
