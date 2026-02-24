'''You are given the root of a binary tree where each node has a value 0 or 1. Each root-to-leaf path represents a binary number starting with the most significant bit.

For example, if the path is 0 -> 1 -> 1 -> 0 -> 1, then this could represent 01101 in binary, which is 13.
For all leaves in the tree, consider the numbers represented by the path from the root to that leaf. Return the sum of these numbers.

The test cases are generated so that the answer fits in a 32-bits integer.

 

Example 1:


Input: root = [1,0,1,0,1,0,1]
Output: 22
Explanation: (100) + (101) + (110) + (111) = 4 + 5 + 6 + 7 = 22
Example 2:

Input: root = [0]
Output: 0'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        def dfs(node: TreeNode, current_value: int) -> int:
            """
            Depth-first search to traverse the tree and calculate path sums.
          
            Args:
                node: Current node in the traversal
                current_value: The accumulated binary value from root to current node
              
            Returns:
                Sum of all binary numbers from this subtree
            """
            # Base case: if node is None, contribute 0 to the sum
            if node is None:
                return 0
          
            # Shift current value left by 1 bit and add current node's value
            # This effectively appends the current bit to the binary number
            current_value = (current_value << 1) | node.val
          
            # If this is a leaf node, return the accumulated binary value
            if node.left is None and node.right is None:
                return current_value
          
            # Recursively calculate sum for left and right subtrees
            left_sum = dfs(node.left, current_value)
            right_sum = dfs(node.right, current_value)
          
            return left_sum + right_sum
      
        # Start DFS from root with initial binary value of 0
        return dfs(root, 0)