class LLNode:
    def __init__ (self, val):
        self.val = val
        self.n = None

class LL:
    def __init__ (self, head):
        self.head = head

    def show (self):
        n = self.head
        while n is not None:
            print n.val,
            n = n.n
        print

    def length (self):
        n = self.head
        count = 0
        while n is not None:
            count = count + 1
            n = n.n

        return count
