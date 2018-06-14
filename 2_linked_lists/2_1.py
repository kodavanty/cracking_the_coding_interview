#!/usr/bin/python

import sys

from ll import LLNode, LL

def ll_remove_dup (l):
    l.show()

    first = l.head
    while first is not None:
        val = first.val
        p = first
        n = p.n
        while p is not None and n is not None:
            if val == n.val: 
                p.n = n.n
                n = n.n
            else:
                p = p.n
                n = n.n

        first = first.n

    print
    l.show()

if __name__ == "__main__":
    head = LLNode(1)
    head.n = LLNode(4)
    head.n.n = LLNode(5)
    head.n.n.n = LLNode(10)
    head.n.n.n.n = LLNode(3)
    head.n.n.n.n.n = LLNode(6)
    head.n.n.n.n.n.n = LLNode(20)
    l = LL(head)

    ll_remove_dup(l)
