'''
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

'''
import time
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        lookup = {}
        for i in range(n):
            tmp = target - nums[i]
            if tmp in lookup:
                return [lookup[tmp], i]
            lookup[nums[i]] = i

if __name__ == '__main__':
    # nums = [2, 7, 11, 15]
    nums = [0, 7, 11, 0]
    target = 0
    start = time.time()
    res = Solution().twoSum(nums,target)
    end = time.time()
    print(start-end)
    print(res)