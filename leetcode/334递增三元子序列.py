class Solution:
    def increasingTriplet(self, nums) -> bool:
        # 动态规划来求解
        #todo  会出现时间超时的提醒。。。
        n = len(nums)
        if n <= 2:
            return False
        dp = [1] * n
        for i in range(n):
            for j in range(i):

                # 动态规划
                # [1,1,1,]  ->>  []
                # 当满足这个值大于上一个值的时候，切换状态
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        lens = max(dp)
        if lens >= 3:
            return True
        else:
            return False

    def increasingTriplet2(self,nums):
        '''
        贪心算法，或者填位置算法
        :param nums:
        :return:
        '''
        # 有三个位置
        import sys
        p1 = sys.maxsize
        p2 = sys.maxsize
        for i in nums:
            if i<=p1:
                p1 = i
            elif i<=p2:
                p2 = i
            else:
                return True

        return False

    def increasingTriplet3(self, nums):
        '''
        二分查找试一下？
        找出最长上升序列，如果大于3就返回True
        :param nums:
        :return:
        '''

        max_increasing = []
        for i in nums:
            low = 0
            height = len(max_increasing)

            while low<height:
                mid = (low+height-1) // 2
                if max_increasing[mid] < i:
                    low = mid+1
                else:
                    height = mid

            print(low)
            if low == len(max_increasing):
                max_increasing.append(i)

            else:
                max_increasing[low] = i
            if len(max_increasing) >= 3:
                return True
        return False






if __name__ == '__main__':
    print(Solution().increasingTriplet3([i for i in range(10000,1,-1)]))