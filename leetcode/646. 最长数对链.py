'''
给出 n 个数对。 在每一个数对中，第一个数字总是比第二个数字小。

现在，我们定义一种跟随关系，当且仅当 b < c 时，数对(c, d) 才可以跟在 (a, b) 后面。我们用这种形式来构造一个数对链。

给定一个对数集合，找出能够形成的最长数对链的长度。你不需要用到所有的数对，你可以以任何顺序选择其中的一些数对来构造。

示例 :

输入: [[1,2], [2,3], [3,4]]
输出: 2
解释: 最长的数对链是 [1,2] -> [3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-length-of-pair-chain
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution:
    def findLongestChain(self, pairs) -> int:
        '''
        可以通过动态规划来求解
        不过超时了。。好尴尬
        :param pairs:
        :return:
        '''
        n = len(pairs)
        pairs = sorted(pairs)  # todo 必须要这步
        print(pairs)
        if not n:
            return 0
        if n==1:
            return 1
        dp = [1]*n
        # todo 动态规划是必须按照规律从小到大，所以要对pairs进行排序？？

        for i in range(n):
            for j in range(i):
                if pairs[i][0]>pairs[j][-1]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

    def findLongestChain2(self, pairs) -> int:
        '''
        贪心算法来解决
        思路是：排序后
        :param pairs:
        :return:
        '''
        link = {}
        for start, end in pairs:
            link[end] = max(link.get(end, float('-inf')), start)
        res = 0
        pre = float('-inf')
        for end in sorted(link.keys()):
            if link[end] > pre:
                res += 1
                pre = end
        return res
    def findLongestChain3(self, pairs) -> int:
        '''
        贪心算法，特别是最开始排序很重要
        :param pairs:
        :return:
        '''
        if not pairs:
            return 0
        sort = sorted(pairs, key=lambda x: (x[1], x[0]), reverse=False)
        print(sort)
        res = [sort[0]]
        for i in range(1, len(sort)):
            if sort[i][0] > res[-1][1]:
                res.append(sort[i])
        return len(res)

if __name__ == '__main__':
    print(Solution().findLongestChain([[1,2], [2,3], [3,4]]))
    print(Solution().findLongestChain2([[3,4],[2,3],[1,2],[1,3,4]]))  # 2

