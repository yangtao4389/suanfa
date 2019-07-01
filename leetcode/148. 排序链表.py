'''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5


'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        '''插入排序
        会超出时间限制。。尴尬了。
        '''
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:  # 这里是O（n）
            if head.val <= head.next.val:
                head = head.next
                continue

            tmp_value = head.next.val
            prev = dummy

            while tmp_value>prev.next.val:
                # 这里思O（n^2***）  1+2+3+。。+n
                #
                prev = prev.next

            sort_node = head.next
            head.next = sort_node.next
            sort_node.next = prev.next
            prev.next = sort_node

        return dummy.next


    def sortList2(self, head: ListNode) -> ListNode:
        # 找到中点
        slow = head
        fast = head
        # 使用这种方式，当结点个数为 2 个时候，slow 在左结点
        # 不会导致死循环
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        head2 = slow.next
        slow.next = None

        lnode = self.sortList(head)
        rnode = self.sortList(head2)

        return self.__merge_two_sorted_list(lnode, rnode)

    def __merge_two_sorted_list(self, head1, head2):
        if head1 is None:
            return head2
        if head2 is None:
            return head1

        if head1.val < head2.val:
            head1.next = self.__merge_two_sorted_list(head1.next, head2)
            return head1
        else:
            head2.next = self.__merge_two_sorted_list(head1, head2.next)
            return head2









































