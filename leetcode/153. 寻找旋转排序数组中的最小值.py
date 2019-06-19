'''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0

'''

class Solution:
    def findMin(self, nums) -> int:
        if not nums:
            return
        return min(nums)
    def findMin2(self, nums) -> int:
        if not nums:
            return
        return sorted(nums)[0]

    def findMin3(self,nums):
        '''
        这种最快，2分查找？
        由于数组仅翻转了一次，可以看做是两段有序数组，并且第一段数组的所有值都比第二段的都大，此时有三种情况：

        我们将数组一分为二，如果左边界比中间大，则最小值在左边；
        如果中间比右边界大，则最小值在右边；
        如果数组有序，则左边界则为最小值。

        :param nums:
        :return:
        '''
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

            print(left)
        return nums[left]


if __name__ == '__main__':
    # print(Solution().findMin3([4,5,6,7,1,2]))
    print(Solution().findMin3([0,1,2,4,5,6,7]))