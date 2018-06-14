#!/usr/bin/python

import sys

from collections import deque
from btree import BTree, BTreeNode
from ll import LLNode, LL

'''
'''
def ll_from_btree (tree):
    nodes = deque([tree.head])
    count = 1
    level = 0
    
    ll = []

    while len(nodes):
        level = level + 1
        count = len(nodes)

        head = None
        tail = None

        while count:
            n = nodes.popleft()

            lnode = LLNode(n.val)
            if head is None:
                head = lnode
                tail = head
            else:
                tail.n = lnode
                tail = lnode

            if n.l is not None:
                nodes.append(n.l)
            if n.r is not None:
                nodes.append(n.r)

            count = count - 1

        l = LL(head)
        ll.append(l)
        
    for l in ll:
        l.show()

if __name__ == "__main__":
    head = BTreeNode(10)
    head.l = BTreeNode(5)
    head.r = BTreeNode(7)
    head.l.l = BTreeNode(6)
    head.l.r = BTreeNode(20)
    head.r.l = BTreeNode(18)
    head.r.r = BTreeNode(30)
    head.r.r.r = BTreeNode(50)
    head.r.r.r.r = BTreeNode(60)
    head.r.r.r.l = BTreeNode(70)

    tree = BTree(head)
    tree.show()
    ll_from_btree(tree)
