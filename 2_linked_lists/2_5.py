#!/usr/bin/python

import sys

from ll import LLNode, LL

'''
'''

def pad_zeros (num, k):
    h = num.head
    print k
    while k:
        t = LLNode(0)
        t.n = h
        h = t
        k = k - 1

    num.head = h

def ll_number_add_wrap (n1, n2):
    if n1 is None and n2 is None:
        return 0, None

    carry, node = ll_number_add_wrap(n1.n, n2.n)

    tnode = LLNode((n1.val + n2.val + carry)%10)
    tnode.n = node

    return (n1.val + n2.val + carry)/10, tnode

def ll_number_add (num1, num2):
    l1 = num1.length()
    l2 = num2.length()

    if l1 > l2:
        pad_zeros(num2, l1-l2)
    if l2 > l1:
        pad_zeros(num1, l2-l1)

    num1.show()
    num2.show()

    carry, node = ll_number_add_wrap(num1.head, num2.head)

    num3 = LL(node)
    if carry:
        tnode = LLNode(carry)
        tnode.n = node
        num3 = LL(tnode)
        
    num3.show()

def ll_number_add_rev (num1, num2):
    num1.show()
    num2.show()

    h1 = num1.head
    h2 = num2.head

    h3 = None
    tail = None
    c = 0
    while h1 is not None or h2 is not None:
        v1 = h1.val if h1 is not None else 0
        v2 = h2.val if h2 is not None else 0

        v = (v1 + v2 + c)%10
        c = (v1 + v2 + c)/10
        if h3 is None:
            h3 = LLNode(v)
            tail = h3
        else:
            tail.n = LLNode(v)
            tail = tail.n

        h1 = h1.n if h1 is not None else None
        h2 = h2.n if h2 is not None else None
     
    if c:
        tail.n = LLNode(c)
    
    LL(h3).show()

if __name__ == "__main__":
    num1 = LLNode(9)
    num1.n = LLNode(5)
    num1.n.n = LLNode(7)
    num1.n.n.n = LLNode(8)

    num2 = LLNode(9)
    num2.n = LLNode(6)
    num2.n.n = LLNode(5)
    num2.n.n.n = LLNode(3)

    #ll_number_add_rev(LL(num1), LL(num2))
    ll_number_add(LL(num1), LL(num2))
