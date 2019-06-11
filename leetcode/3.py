'''
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        left = 0
        lookup = set()  # 唯一集合
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len: max_len = cur_len
            lookup.add(s[i])
            print(lookup)
        return max_len

    def length_2(self,s:str)->int:
        if not s :return 0
        #  "abcabcbb"
        _no_loop_set = set()
        _length = 0
        _cur_max_length = 0

        for i in range(len(s)):
            _length += 1
            if s[i] in _no_loop_set:
                _no_loop_set.remove(s[i])


            _no_loop_set.add(s[i])
            _cur_max_length = len(_no_loop_set)




if __name__ == '__main__':
    str1 = "abcabcbbc"
    a = Solution().lengthOfLongestSubstring(str1)
    a = Solution().length_2(str1)
    print(a)