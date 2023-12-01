class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr =  ListNode(homepage)
        

    def visit(self, url: str) -> None:
        self.curr.next = ListNode(url, self.curr)
        self.curr = self.curr.next

    def back(self, steps: int) -> str:
        while self.curr.prev and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        return self.curr.val
        

    def forward(self, steps: int) -> str:
        while self.curr.next and steps > 0:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val

homepage = 'leetcode.com'
browser_history = BrowserHistory(homepage)

# Visit some URLs
browser_history.visit('google.com')
browser_history.visit('facebook.com')
browser_history.visit('youtube.com')

# Go back and forward in history
print(browser_history.back(1))  # Should return 'facebook.com'
print(browser_history.back(1))  # Should return 'google.com'
print(browser_history.forward(1))  # Should return 'facebook.com'

# Visit a new URL
browser_history.visit('linkedin.com')
print(browser_history.forward(2))  # Should not move forward and return 'linkedin.com'
print(browser_history.back(2))  # Should return 'google.com'
print(browser_history.back(7))  # Should return 'leetcode.com'
