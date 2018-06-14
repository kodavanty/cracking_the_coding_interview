#!/usr/bin/python

import sys

from ll import LLNode, LL

'''
'''

def ll_partition (l, k):
    l.show()

    n = l.head.n

    head = l.head
    tail = head
    head.n = None

    while n is not None:
        p = n
        n = n.n

        if p.val <= k:
            p.n = head
            head = p
        else:
            p.n = tail.n
            tail.n = p

    print
    LL(head).show()

if __name__ == "__main__":
    head = LLNode(1)
    head.n = LLNode(4)
    head.n.n = LLNode(5)
    head.n.n.n = LLNode(10)
    head.n.n.n.n = LLNode(3)
    head.n.n.n.n.n = LLNode(6)
    head.n.n.n.n.n.n = LLNode(20)
    l = LL(head)
    ll_partition(l, 15)
