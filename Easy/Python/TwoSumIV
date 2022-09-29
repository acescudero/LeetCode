# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        checked = {}
        return self.traversal_helper(root, k, checked)
        
    def traversal_helper(self, node: TreeNode, target, checked):
        return self.traversal_rec(node, target, checked)
    
    def traversal_rec(self, node: TreeNode, target, checked):
        #base case
        if node==None:
            return False
        if target-node.val in checked:
            return True
        else:
            checked[node.val]=True
            found_r = self.traversal_rec(node.right, target,checked)
            found_l = self.traversal_rec(node.left, target, checked)
            
            if found_r or found_l:
                return True
        
        return False
