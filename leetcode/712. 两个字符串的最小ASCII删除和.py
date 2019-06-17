'''

给定两个字符串s1, s2，找到使两个字符串相等所需删除字符的ASCII值的最小和。

示例 1:

输入: s1 = "sea", s2 = "eat"
输出: 231
解释: 在 "sea" 中删除 "s" 并将 "s" 的值(115)加入总和。
在 "eat" 中删除 "t" 并将 116 加入总和。
结束时，两个字符串相等，115 + 116 = 231 就是符合条件的最小和。
示例 2:

输入: s1 = "delete", s2 = "leet"
输出: 403
解释: 在 "delete" 中删除 "dee" 字符串变成 "let"，
将 100[d]+101[e]+101[e] 加入总和。在 "leet" 中删除 "e" 将 101[e] 加入总和。
结束时，两个字符串都等于 "let"，结果即为 100+101+101+101 = 403 。
如果改为将两个字符串转换为 "lee" 或 "eet"，我们会得到 433 或 417 的结果，比答案更大。
注意:

0 < s1.length, s2.length <= 1000。
所有字符串中的字符ASCII值在[97, 122]之间。

'''


class Solution:
    def minimumDeleteSum2(self, s1: str, s2: str) -> int:
        '''
        这种方式不行，因为要满足顺序也必须是一样的。。
        :param s1:
        :param s2:
        :return:
        '''
        from copy import deepcopy
        s1_list = sorted([ord(s) for s in s1])
        s2_list = sorted([ord(s) for s in s2])
        tmp_s2_list = deepcopy(s2_list)
        # 通过这样的转换，就感觉有点像找最大公约数
        print(s1_list)
        print(s2_list)
        tmp_list = [] # 最大公约数
        for num in s1_list:
            if num in tmp_s2_list:
                tmp_list.append(num)
                tmp_s2_list.remove(num)
        print(tmp_list)

        total = sum(s1_list) + sum(s2_list) - 2 * sum(tmp_list) + 2 * tmp_list[0]
        # if len(tmp_list) == len(s1_list) or len(tmp_list) == len(s2_list):
        #     total = sum(s1_list)+sum(s2_list) - 2*sum(tmp_list) +2 * tmp_list[0]
        # else:
        #     total = sum(s1_list)+sum(s2_list) - 2*sum(tmp_list)

        return total

    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        '''
        参考别人写的代码
        :param s1:
        :param s2:
        :return:
        1.s1[i-1] == s2[j-1]，新增的两个字符相等的情况下，没有必要删除之前的结果，因此dp[i][j] = dp[i-1][j-1]
2.s1[i-1] != s2[j-1]，取三者的最小值
（1）保留s2串，删除s1串的字符，dp[i][j] = dp[i-1][j] + s1.charAt(i-1)
（2）保留s1串，删除s2串的字符，dp[i][j] = dp[i][j-1] + s1.charAt(j-1)
（3）删除s1、s2串的字符，dp[i][j] = dp[i-1][j-1] + s1.charAt(i-1) + s2.charAt(j-1)

        这种动态规划，有点类似于多向量求解问题。主要靠的是思维。
        '''
        m, n = len(s1), len(s2)
        dp = [[float('inf') for _ in range(n + 1)] for i in range(m + 1)]      
        dp[0][0] = 0
        for i in range(m):
            dp[i + 1][0] = dp[i][0] + ord(s1[i])
        for i in range(n):
            dp[0][i + 1] = dp[0][i] + ord(s2[i])
        print(dp)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:  # 如果这两个值相等
                    dp[i][j] = dp[i - 1][j - 1] # 该ASCII码值等于上一个
                else:
                    dp[i][j] = min(dp[i - 1][j] + ord(s1[i - 1]), dp[i][j - 1] + ord(s2[j - 1]))  # 等于最小值

        print(dp)
        return dp[-1][-1]

    def minimumDeleteSum3(self, s1: str, s2: str) -> int:
        '''
        自己想想动态规划怎么求解
        :param s1:
        :param s2:
        :return:
        '''
        pass




if __name__ == '__main__':
    print(Solution().minimumDeleteSum("delete", "leet"))  # 403
    print(Solution().minimumDeleteSum("vwojt", "saqhgdrarwntji"))  # 1613
    print(Solution().minimumDeleteSum("a", "at"))  # 116
    print(Solution().minimumDeleteSum("sea", "eat"))  # 231




