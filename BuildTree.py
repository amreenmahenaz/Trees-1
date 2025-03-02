# // Time Complexity :O(n)
# // Space Complexity :O(height)
# // Did this code successfully run on Leetcode :yes
# // Any problem you faced while coding this :no


# // Your code here along with comments explaining your approach
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        VAL_TO_INORDER_IDX = {inorder[i]: i for i in range(len(inorder))}

        def buildTreePartition(preorder, inorder_start, inorder_end):
            if not preorder or inorder_start < 0 or inorder_end > len(inorder):
                return None

            root_val = preorder[0]
            root_inorder_idx = VAL_TO_INORDER_IDX[root_val]
            if root_inorder_idx > inorder_end or root_inorder_idx < inorder_start:
                return None
            
            root = TreeNode(preorder.pop(0))
            root.left = buildTreePartition(preorder, inorder_start, root_inorder_idx - 1)
            root.right = buildTreePartition(preorder, root_inorder_idx + 1, inorder_end)

            return root

        return buildTreePartition(preorder, 0, len(inorder) - 1)