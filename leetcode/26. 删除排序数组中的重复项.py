'''
给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。

示例 1:

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。
示例 2:

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。
说明:

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以“引用”方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

// nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
int len = removeDuplicates(nums);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中该长度范围内的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

'''
class Solution:
    def removeDuplicates(self, nums) -> int:
        '''
        会超时
        :param nums:
        :return:
        '''
        for i in range(len(nums)-1,0,-1):
            if nums[i] in nums[:i]:
                del nums[i]
            # print(nums)
        return len(nums)

    def removeDuplicates2(self, nums) -> int:
        '''
        题目规定是排序数组
        使用双指针方法..
        j指针为不重复的数组，当i跟j不等的时候，变化j的指针
        :param nums:
        :return:
        '''
        j = 0
        if len(nums)<=1:
            return len(nums)
        for i in range(1,len(nums)):
            if nums[i] != nums[j]:
                j += 1
                nums[j] = nums[i]
        print(nums)
        return j+1


if __name__ == '__main__':
    print(Solution().removeDuplicates2([0,0,1,1,1,2,2,3,3,4]))
    print(Solution().removeDuplicates2([0,0,1,4]))
    print(Solution().removeDuplicates2([0,0]))
