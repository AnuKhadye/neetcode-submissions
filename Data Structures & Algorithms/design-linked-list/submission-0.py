class ListNode:
    def __init__(self, val=0, next=None):
        self.val =val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        cur = self.head
        for _ in range(index):
            if not cur:
                return -1
            cur = cur.next
        return cur.val if cur else -1

    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val: int) -> None:
        if self.head is None:
            self.addAtHead(val)
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        for i in range(index - 1):
            cur = cur.next
        newNode = ListNode(val)
        newNode.next = cur.next
        cur.next = newNode
        self.size += 1

    
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
            self.size -= 1
            return
        cur = self.head
        for i in range(index - 1):
            cur = cur.next
        cur.next = cur.next.next
        self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)