'''
利用分治法，找到[-2,1,-3,4,-1,2,1,-5,4]   连续子数组 [4,-1,2,1] 的和最大，为 6。

寻找子数组A[low..high] 中的最大连续子数组A[i...j]
将A[low..high] 求出中央位置，mid，分解为A[low.. mid]  A[mid+1...high]
   这样A[i..j] 所处的位置必然是下面三种情况：
1、完全位于A[low..mid]
2、完全位于A[mid+1...high]
3、跨域了中点mid

'''

import sys
# 找到跨越中点的数组。
def find_max_crossing_subarray(A,low,mid,high):
    '''

    :param A:  数组
    :param low:
    :param mid:
    :param high:
    :return:
    '''
    left_sum = -sys.maxsize-1
    max_left =low
    max_right=high
    sum_n = 0
    for i in range(mid,low-1,-1):
        sum_n = sum_n+A[i]
        if sum_n>left_sum:
            left_sum = sum_n
            max_left = i

    right_sum = -sys.maxsize -1
    sum_n = 0
    for j in range(mid+1,high+1):
        sum_n = sum_n + A[j]
        if sum_n>right_sum:
            right_sum = sum_n
            max_right = j

    return (max_left,max_right,left_sum+right_sum)


def find_maxmum_subarray(A,low,high):
    if high == low:
        return (low,high,A[low])
    mid = (low+high)//2
    (left_low,left_high,left_sum) = find_maxmum_subarray(A,low,mid)
    (right_low,right_high,right_sum) = find_maxmum_subarray(A,mid+1,high)
    (cross_low,cross_high,cross_sum) = find_max_crossing_subarray(A,low,mid,high)

    if left_sum>=right_sum and left_sum>= cross_sum:
        return (left_low,left_high,left_sum)
    elif right_sum>=left_sum and right_sum>=cross_sum:
        return  (right_low,right_high,right_sum)
    else:
        return (cross_low,cross_high,cross_sum)


if __name__ == '__main__':
    # A = [-2,1,-3,4,-1,2,1,-5,4]
    A = [1,2]
    low = 0
    high = len(A)-1
    print(find_maxmum_subarray(A,low,high))









