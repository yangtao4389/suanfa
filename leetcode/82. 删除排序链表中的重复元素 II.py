'''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        '''
        迭代
        :param head:
        :return:
        '''
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1000)
        dummy.next = head
        slow = dummy
        fast = dummy.next
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next

    def deleteDuplicates2(self, head: ListNode) -> ListNode:
        '''
        感觉会用到两个循环
        假设第一个virtual_node为自己创建的，node后面跟head
        快指针指向head.next  慢指针指向head
        当 head存在，循环遍历head.next  如果存在，判断是否相等。如果不等，head为head.next  慢指针指向head 快指针指向head.next

        :param head:
        :return:
        '''
        if not head or not head.next:
            return head
        virtual_node = ListNode(-1000)
        virtual_node.next = head
        slow_pointer = virtual_node
        fast_pointer = head

        while fast_pointer:
            slow_pointer.next = fast_pointer
            fast_pointer = fast_pointer.next


    def deleteDuplicates3(self, head: ListNode) -> ListNode:
        '''
        递归来解决一下
        :param head:
        :return:
        '''
        if not head: return head
        if head.next and head.val == head.next.val:
            while head.next != None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
        return head

    def deleteDuplicates4(self, head: ListNode) -> ListNode:
        '''
        递归来解决一下
        :param head:
        :return:
        '''
        if not head:
            return head
        if head.next and head.val == head.next.val:
            while head.next != None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates4(head.next)
        else:
            pass






























