'''
给定两个单词 word1 和 word2，找到使得 word1 和 word2 相同所需的最小步数，每步可以删除任意一个字符串中的一个字符。

示例 1:

输入: "sea", "eat"
输出: 2
解释: 第一步将"sea"变为"ea"，第二步将"eat"变为"ea"
说明:

给定单词的长度不超过500。
给定单词中的字符只含有小写字母。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-operation-for-two-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1),len(word2)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        print(dp)
        for i in range(1,n+1):
            for j in range(1,m+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j],dp[i][j-1])

        print(dp)
        return n+m-2*dp[n][m]

    def minDistance2(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        dp = []
'''
这道题跟 712求两个字符串的最小ASCII删除和 一样的逻辑。其实动态规划这种算法确实可以解决很多问题，不过我掌握的是一阶动态，二阶动态有点没摸透
关于动态规划
就是先生成相应的dp
当前dp的状态是由几个条件来判断就ok
像上面这道题，当前dp状态就跟对角线一个，左上一个，顶部一个。
'''
if __name__ == '__main__':
    print(Solution().minDistance("sea","eatd"))