#!/usr/local/anaconda3/bin/python

from typing import List

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if preorder is None or inorder is None:
            return None
        if len(preorder) == 0 or len(inorder) == 0:
            return None
        root_value = preorder[0]
        root = TreeNode(root_value)
        mid = inorder.index(root_value)
        root.left = self.buildTree(preorder[1: mid+1], inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root

if __name__ == "__main__":
   s = Solution()
   print(s.buildTree([3,9,20,15,7],[9,3,15,20,7]))