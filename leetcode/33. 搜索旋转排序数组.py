'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:

输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4
示例 2:

输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1

'''

class Solution:
    def search(self, nums, target: int) -> int:
        '''
        因为时间复杂度必须是 O(log n) 级别  则直接找最小值？？
        :param nums:
        :param target:
        :return:
        '''
        try:
            return nums.index(target)  # 时间复杂度为O(1)
        except:
            return -1
if __name__ == '__main__':
    print(Solution().search([1,3],3))