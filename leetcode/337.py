# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
# class Solution:
#     def rob(self, root: TreeNode) -> int:
#         if root == None:
#             return 0
#         def helper(root):
#             if root == None:
#                 return [0,0]
#             left = helper(root.left)
#             right = helper(root.right)
#             rob = root.val + left[1] +right[1]
#             skip = max(left) +max(right)
#             return [rob,skip]
#         res = helper(root)
#         return max(res)


# class Solution:
#     def rob(self, root):
#         """
#         :type root: TreeNode
#         :rtype: int
#         """
#         stack = [(0, root)]
#         result = {None: (0, 0)}
#         while stack:
#             rob, node = stack.pop()
#             if not node:
#                 continue
#
#             if not rob:
#                 stack.extend([(1, node), (0, node.right), (0, node.left)])
#             else:
#                 result[node] = (result[node.left][1] + result[node.right][1] + node.val, \
#                                 max(result[node.left]) + max(result[node.right]))
#         return max(result[root])


class ReturnType:
    def __init__(self, lai, bulai):
        self.lai = lai
        self.bu = bulai

class Solution:
    def process(self, node):
        lai = node.val
        bu = 0
        if node.left:
            resT = self.process(node.left)
            lai += resT.bu
            bu += max(resT.lai, resT.bu)
        if node.right:
            resT = self.process(node.right)
            lai += resT.bu
            bu += max(resT.lai, resT.bu)
        return ReturnType(lai, bu)

    def rob(self, root):
        if not root:
            return 0
        restype = self.process(root)
        return max(restype.lai, restype.bu)

if __name__ == '__main__':
    t = TreeNode(1)
    left1 = TreeNode(2)
    left2 = TreeNode(3)
    right1 = TreeNode(4)
    right2 = TreeNode(5)
    t.left = left1
    left1.left=left2
    t.right = right1
    right1.right = right2
    ret = Solution().rob(t)
    print(ret)