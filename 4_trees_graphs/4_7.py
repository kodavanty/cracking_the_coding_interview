#!/usr/bin/python

import sys

from btree import BTree, BTreeNode

'''
'''

def is_child (node, key):
    if node is None:
        return False

    if node.val == key:
        return True

    return is_child(node.l, key) or is_child(node.r, key)

def common_ancestor (node, key1, key2):

    if node is None:
        return None

    if node.val == key1 or node.val == key2: 
        return node

    is_left1 = is_child(node.l, key1)
    is_left2 = is_child(node.l, key2)

    if is_left1 != is_left2:
        return node

    tmp = node.l if is_left1 else node.r

    return common_ancestor(tmp, key1, key2)

def common_ancestor_helper (tree, key1, key2):
    n = common_ancestor(tree.head, key1, key2)
    print n.val

if __name__ == "__main__":
    head = BTreeNode(30)
    head.l = BTreeNode(25)
    head.r = BTreeNode(35)
    head.l.p = head
    head.r.p = head

    head.l.l = BTreeNode(20)
    head.l.r = BTreeNode(27)
    head.l.l.p = head.l
    head.l.r.p = head.l

    head.l.r.l = BTreeNode(26)
    head.l.r.l.p = head.l.r

    head.r.l = BTreeNode(32)
    head.r.r = BTreeNode(40)
    head.r.l.p = head.r
    head.r.r.p = head.r

    head.r.r.l = BTreeNode(37)
    head.r.r.l.p = head.r.r

    tree = BTree(head)
    tree.show()
    common_ancestor_helper(tree, 26, 37)
