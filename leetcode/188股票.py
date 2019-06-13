class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        # dp = [[[0]*2 for _ in range(3)] for i in range(n)]
        max_k = k
        if max_k >= n/2:
            # 限制无效，则为求最大值
            return self.maxProfitNoLimit(prices)
        dp = [[[0 for _ in range(2)] for _ in range(max_k + 1)] for _ in range(len(prices))]
        for i in range(n):
            for k in range(1, max_k + 1):
                if i - 1 == -1:
                    dp[i][k][0] = dp[i][k][0] = 0
                    dp[i][k][1] = dp[i][k][1] = -prices[i]

                    continue

                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        return dp[n - 1][max_k][0]

    def maxProfitNoLimit(self, prices: list) -> int:
        dp = [([0] * 2) for i in range(len(prices))]
        for i in range(len(prices)):
            if i-1 ==-1:
                dp[i][0] = 0
                dp[i][1] = -prices[i]
                continue

            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1],-prices[i])
        print(dp)
        return dp[len(prices)-1][0]