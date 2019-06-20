'''
删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        '''
        双指针？？ 当val跟要删除的一样时，
        :param head:
        :param val:
        :return:
        '''
        curr = head
        while (curr != None and curr.next != None):
            if (curr.next.val == val):
                curr.next = curr.next.next
            else:
                curr = curr.next
        if (head != None and head.val == val):
            head = head.next
        return head