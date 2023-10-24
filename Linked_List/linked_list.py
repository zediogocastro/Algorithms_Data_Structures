class ListNode:

    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head

    def get(self, index: int) -> int:
        cur = self.head.next
        i = 0
        while cur:
            if i == index:
                return cur.val
            i += 1
            curr = curr.next
        return -1 


x = LinkedList()
print(x.head.next)