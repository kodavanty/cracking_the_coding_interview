#!/usr/bin/python

import sys

from ll import LLNode, LL

'''
'''

def ll_kth (l, k):
    l.show()

    first = l.head
    second = l.head

    for i in range(k):
        first = first.n

    while first is not None:
        first = first.n
        second = second.n

    print "Kth node is (%u)" % second.val


if __name__ == "__main__":
    head = LLNode(1)
    head.n = LLNode(4)
    head.n.n = LLNode(5)
    head.n.n.n = LLNode(10)
    head.n.n.n.n = LLNode(3)
    head.n.n.n.n.n = LLNode(6)
    head.n.n.n.n.n.n = LLNode(20)
    l = LL(head)
    ll_kth(l, 3)
