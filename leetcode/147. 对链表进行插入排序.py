'''
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
 

示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5

'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        '''
        可以用递归嘛？ 好像很难，没想出来
        :param head:
        :return:
        '''
        if not head:
            return head
        if head.next and head.next.val < head.val:
            head.next = head
            head = head.next
            return self.insertionSortList(head.next)
        else:
            return self.insertionSortList(head.next)

    def insertionSortList2(self, head: ListNode) -> ListNode:
        '''
        直接使用插入排序
        :param head:
        :return:
        '''
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        while head and head.next:
            if head.val <= head.next.val:
                head = head.next
                continue
            pre = dummy
            while pre.next.val < head.next.val:
                pre = pre.next
            cur = head.next
            head.next = cur.next
            cur.next = pre.next
            pre.next = cur

        return dummy.next

    def insertionSortList3(self, head: ListNode) -> ListNode:
        '''
        善用变量来解决
        :param head:
        :return:
        '''
        # 对于整个链条的遍历
        if not head or not head.next:
            return head

        dummy = ListNode(0)
        dummy.next = head

        while head and head.next:
            # 当整个链条都是有序状态，
            if head.val <= head.next.val:
                head = head.next
                continue

            # 非有序的处理 1-》0  0需要搜索后 排到一个位置 当前head是在1上面，0代表head.next.val
            tmp_value = head.next.val
            # 将该值从列表头开始比，一直会比到当前head dummy 为虚拟-1位 接下来一位为head
            # 每次都跟dummy.next 对比，当遇到大于的时候停下，此时dummy就为插入的位置
            prev = dummy
            while tmp_value > prev.next.val:
                prev = prev.next

            # 将该节点插入到dummy的当前位置
            # 拿来被排序的节点 head.next
            sort_node = head.next
            # 对于整个链条的遍历：
            head.next = sort_node.next
            # 对于sort_node 位置的放入
            sort_node.next = prev.next # 后
            prev.next = sort_node  # 前
        return dummy.next

























