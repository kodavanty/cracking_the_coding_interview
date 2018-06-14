#!/usr/bin/python

import sys

from collections import deque
from btree import BTree, BTreeNode
from ll import LLNode, LL

'''
'''
def is_bst_helper (node):
    if node is None:
        return True

    bst = True
    if node.l is not None:
        bst = bst and (node.val >= node.l.val)
    if node.r is not None:
        bst = bst and (node.val < node.r.val)

    return bst and is_bst_helper(node.l) and is_bst_helper(node.r)

def is_bst (tree):
    print is_bst_helper(tree.head)

if __name__ == "__main__":
    head = BTreeNode(60)
    head.l = BTreeNode(25)
    head.r = BTreeNode(35)
    head.l.l = BTreeNode(20)
    head.l.r = BTreeNode(27)
    #head.r.l = BTreeNode(32)
    head.r.r = BTreeNode(40)

    tree = BTree(head)
    tree.show()
    is_bst(tree)
