#!/usr/bin/python

import sys

from ll import LLNode, LL

'''
'''

def ll_palindrome (l):
    l.show()

    fast = l.head
    slow = l.head

    nodes = [slow]
    while fast is not None and fast.n is not None:
        fast = fast.n.n
        slow = slow.n
        nodes.append(slow)

    while slow is not None:
        node = nodes.pop()
        if node.val != slow.val:
            return False
        slow = slow.n

    return True

if __name__ == "__main__":
    head = LLNode(1)
    head.n = LLNode(4)
    head.n.n = LLNode(5)
    head.n.n.n = LLNode(10)
    head.n.n.n.n = LLNode(5)
    head.n.n.n.n.n = LLNode(4)
    head.n.n.n.n.n.n = LLNode(1)
    l = LL(head)
    print ll_palindrome(l)
