'''
参考链接
https://mp.weixin.qq.com/s?__biz=MzU0MDg5OTYyOQ==&mid=100000392&idx=1&sn=3eb48be6e6da484490f1bd848df86a96&chksm=7b3362ca4c44ebdc6a757bc60e859021fdd56c7c3e5dd54992bf4e2d50a30f7ec561ce3b36f6#rd

'''

# 创建三维数组
# dp = [([None]*3) for i in range(10)]
class Solution:
    def maxProfit(self, prices: list) -> int:
        dp = [([None] * 2) for i in range(len(prices))]
        for i in range(len(prices)):
            if i-1 ==-1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue

            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        print(dp)
        return dp[len(prices)-1][0]


if __name__ == '__main__':
    a = [7,6,5,4,3,2]
    b = Solution().maxProfit(a)
    print(b)