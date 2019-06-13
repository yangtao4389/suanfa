class Solution:
    # 将 dp 数组定义为：以 nums[i] 结尾的最长上升子序列的长度
    # 那么题目要求的，就是这个 dp 数组中的最大者
    # 以数组  [10, 9, 2, 5, 3, 7, 101, 18] 为例
    # dp 的值： 1  1  1  2  2  3  4    4

    def lengthOfLIS(self, nums):
        size = len(nums)
        # 特判
        if size <= 1:
            return size

        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    # + 1 的位置不要加错了
                    dp[i] = max(dp[i], dp[j] + 1)
        # 最后要全部一看遍，取最大值
        return max(dp)


    def lenth_of_lis(self,nums):
        '''
        动态规划，状态转移。先用一个数组存储所有状态。
        遍历，再遍历之前的。如果遇到
        :param nums:
        :return:
        '''
        n = len(nums)
        if n <=1:
            return n

        dp = [1]*n
        for i in range(1,n):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
                print(dp)

        return max(dp)

    def lenth_of_lis2(self,nums):
        '''
        二分查找 跟贪婪算法
        :param nums:
        :return:
        '''

        size = len(nums)
        if size < 2:
            return size

        tail = []
        for num in nums:
            # 找到大于等于 num 的第 1 个数
            l = 0
            r = len(tail)
            while l < r:
                mid = l + (r - l) // 2
                if tail[mid] < num:
                    l = mid + 1
                else:
                    r = mid
            if l == len(tail):
                tail.append(num)
            else:
                print(l,r)
                tail[l] = num

        return len(tail)

    def lenth_of_lis3(self, nums):
        '''
        假设全部增长
        :param nums:
        :return:
        '''
        import sys
        n = len(nums)
        increase_list = [sys.maxsize]*n
        for num in nums:
            for j in range(len(increase_list)):
                if num <= increase_list[j]:
                    increase_list[j] = num
                    break

        print(increase_list)
        try:
             return increase_list.index(sys.maxsize)
        except:
            return n








if __name__ == '__main__':
    print(Solution().lenth_of_lis3([10,9,2,5,3,7,101,18]))




