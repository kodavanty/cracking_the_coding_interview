#!/usr/bin/python

import sys

from btree import BTree, BTreeNode

'''
'''

def sum_path (node, k, l, paths):
    if node is None:
        return

    l.append(node.val)
    sum_path(node.l, k, l, paths)
    sum_path(node.r, k, l, paths)

    s = 0
    for i in range(len(l)-1, -1, -1):
        s = s + l[i]
        if s == k:
            paths.append(l[i:len(l)])

    l.pop() 

def tree_sum (tree, s):
    l = []
    paths = []
    sum_path(tree.head, s, l, paths)
    print paths

if __name__ == "__main__":
    head = BTreeNode(30)

    head.l = BTreeNode(25)
    head.r = BTreeNode(35)

    head.l.l = BTreeNode(20)
    head.l.r = BTreeNode(27)

    head.l.r.l = BTreeNode(26)
    head.l.r.l.l = BTreeNode(34)

    head.r.l = BTreeNode(32)
    head.r.r = BTreeNode(40)

    head.r.r.l = BTreeNode(37)

    tree = BTree(head)
    tree.show()
    tree_sum(tree, 112)
