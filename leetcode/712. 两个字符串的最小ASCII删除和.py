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
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
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

    def minimumDeleteSum2(self, s1: str, s2: str) -> int:





if __name__ == '__main__':

    print(Solution().minimumDeleteSum( "delete","leet"))   # 403
    print(Solution().minimumDeleteSum( "vwojt","saqhgdrarwntji"))  #1613
    print(Solution().minimumDeleteSum("a","at"))  #     116
    print(Solution().minimumDeleteSum("sea","eat"))  #     231



