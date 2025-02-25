'''
给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:

输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''


class Solution:
    def findLengthOfLCIS(self, nums) -> int:
        max_length = 0
        temp_length = 1
        n = len(nums)
        if n <=1:
            return 1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                temp_length += 1
            else:
                temp_length = 1
            max_length = max(max_length, temp_length)
        return max_length

if __name__ == '__main__':
    print(Solution().findLengthOfLCIS([1,3,5,2,37,9,9,3,78]))
