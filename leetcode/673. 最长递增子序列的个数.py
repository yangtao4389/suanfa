'''
给定一个未排序的整数数组，找到最长递增子序列的个数。

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findNumberOfLIS(self, nums) -> int:
        '''
        根据300  dp 动态规划来找？时间最长了
        比方[1,3,5,7,5,8]
        dp为[1,2,3,4,3,5]  最长为5，找到所有5的个数
        :param nums:
        :return:
        '''
        n = len(nums)
        dp = [1]*n
        dp_collection = [1]*n  # 组合数
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j]:
                    if dp[i] < dp[j]+1:
                        dp[i] = dp[j]+1
                        dp_collection[i]  = dp_collection[j]  # collection 变的两条准则
                    elif dp[i] == dp[j]+1:
                        dp_collection[i] += dp_collection[j]

                    # dp[i] = max(dp[i],dp[j]+1)

        print(dp)
        print(dp_collection)
        res = 0
        max_dp = max(dp)
        for i in range(n):
            if dp[i] == max_dp:
               res += dp_collection[i]

        return res

    def findNumberOfLIS2(self, nums):

        """
        这种算法比上面那种快10倍。。
        :type nums: List[int]
        :rtype: int
        """
        import collections
        if not nums:
            return 0
        l = len(nums)
        dq = list()
        totals = list()
        for num in nums:
            index = len(dq) - 1
            if not dq or num > dq[-1]:
                dq.append(num)
                totals.append(collections.defaultdict(int))
            else:
                # 这里比较厉害
                while index >= 0 and dq[index] >= num:
                    index -= 1
                dq[index + 1] = num
            if not index + 1:
                totals[index + 1][num] += 1
            else:
                # 这步很难理解。。写的这么狂野。。
                totals[index + 1][num] += sum([val for key, val in totals[index].items() if key < num])
        print(dq)
        print(totals)
        return sum(totals[-1].values())



if __name__ == '__main__':
    print(Solution().findNumberOfLIS([1,3,5,4,7,2,2,3,3,4,4,5]))
    print("\n")
    print(Solution().findNumberOfLIS2([1,2,2,3,3,4]))

