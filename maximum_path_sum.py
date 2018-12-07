#Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
#     def getLeftChild(self):
#         return self.left
#     def getRightChild(self):
#         return self.right
#     def setNodeValue(self,value):
#         self.rootid = value
#     def getNodeValue(self):
#         return self.rootid     
class Solution:

    def height(self, root):
        if root==None:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        return max(root.val+lh, root.val+rh)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root==None:
            return 0

        lh = self.height(root.left)
        rh = self.height(root.right)

        ld =  self.maxPathSum(root.left)
        rd =  self.maxPathSum(root.right)

        return max(lh+rh+root.val, max(ld , rd))
    
#root=TreeNode(0)
   
root=TreeNode(2)
root.left=TreeNode(4)
root.right=TreeNode(6)
root.left.left = TreeNode(8) 
root.left.right = TreeNode(10) 


 
    
#root=TreeNode(5)
#root.left=TreeNode(2)
#root.right=TreeNode(1)
#root.val
#root.left.val
#root.right.val
#


sol=Solution()
sol.height(root)

sol.maxPathSum(root)


