class ListNode:
    def __init__(self, url, prev=None, next=None):
        self.url = url
        self.prev = prev
        self.next = next


class BrowserHistory:
    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)

    def visit(self, url: str) -> None:
        newNode = ListNode(url, prev=self.cur, next=None)
        self.cur.next = newNode
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.prev == None:
                return self.cur.url
            self.cur = self.cur.prev
        return self.cur.url       


    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if self.cur.next == None:
                return self.cur.url
            self.cur = self.cur.next
        return self.cur.url



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
