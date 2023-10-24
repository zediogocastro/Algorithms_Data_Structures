from typing import Optional

# Solution for reversing a linked list

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# Tests for the above solution
import unittest

class TestReverseLinkedList(unittest.TestCase):

    def setUp(self):
        self.solver = Solution()

    def list_to_linked_list(self, nums):
        if not nums:
            return None
        head = ListNode(nums[0])
        current = head
        for num in nums[1:]:
            current.next = ListNode(num)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        return nums

    def test_example_1(self):
        nums = [1, 2, 3, 4, 5]
        expected = [5, 4, 3, 2, 1]
        head = self.list_to_linked_list(nums)
        reversed_head = self.solver.reverseList(head)
        actual = self.linked_list_to_list(reversed_head)
        self.assertEqual(actual, expected)

    def test_example_2(self):
        nums = [1, 2]
        expected = [2, 1]
        head = self.list_to_linked_list(nums)
        reversed_head = self.solver.reverseList(head)
        actual = self.linked_list_to_list(reversed_head)
        self.assertEqual(actual, expected)

# This ensures tests run if this file is executed directly
if __name__ == '__main__':
    unittest.main()
