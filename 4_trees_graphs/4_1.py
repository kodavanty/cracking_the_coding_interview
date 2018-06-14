#!/usr/bin/python

import sys

from btree import BTree, BTreeNode

'''
'''
def is_balanced (n):
    if n is None:
        return 0, "BALANCED"

    if n.l is None and n.r is None:
        return 1, "BALANCED"

    left_height, left_balanced = is_balanced(n.l)
    right_height, right_balanced = is_balanced(n.r)

    height = max(left_height, right_height)+1
    if abs(left_height - right_height) > 1:
        return height, "NOT BALANCED"
    return height, "BALANCED"

def balanced_btree (tree):
    height, balanced = is_balanced(tree.head)
    print height, balanced

if __name__ == "__main__":
    head = BTreeNode(10)
    head.l = BTreeNode(5)
    head.r = BTreeNode(7)
    head.l.l = BTreeNode(6)
    head.l.r = BTreeNode(20)
    head.r.l = BTreeNode(18)
    head.r.r = BTreeNode(30)
    '''
    head.r.r.r = BTreeNode(50)
    head.r.r.r.r = BTreeNode(60)
    '''

    tree = BTree(head)
    tree.show()
    balanced_btree(tree)
