#!/usr/bin/python

import sys

from btree import BTree, BTreeNode

'''
'''

def left_most_child (node):
    if node is None:
        return None

    while node.l is not None:
        node = node.l

    return node

def inorder_successor (node):
    '''
        If node has right child then the successor is the left most child of
        the right node.
        If the node does not have a right child. If the node is to the left of
        it's parent, the parent is the successor. If the node is to the right
        of it's parent then the parent subtree is also traversed. We need to 
        find a parent node with the right subtree untraversed. We need to find
        a node which is the left of it's parent.
    '''
    if node.r is not None:
        return left_most_child(node.r)

    m = node.p
    while m and m.l is not node:
        node = node.p
        m = node.p

    return m

def inorder_successor_helper (tree):
    head = tree.head

    while head.l is not None:
        head = head.l

    first = head

    while first is not None:
        print first.val,
        first = inorder_successor(first)

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
    inorder_successor_helper(tree)
