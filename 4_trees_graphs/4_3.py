#!/usr/bin/python

import sys

from btree import BTree, BTreeNode

'''
'''
def create_btree_helper (array, start, end):
    if start > end:
        return None

    mid = (start + end)/2

    n = BTreeNode(array[mid])
    n.l = create_btree_helper(array, start, mid-1)
    n.r = create_btree_helper(array, mid+1, end)

    return n

def create_btree (array):
    head = create_btree_helper(array, 0, len(array)-1)
    tree = BTree(head)
    tree.show()

if __name__ == "__main__":
    create_btree([14, 24, 39, 50, 55, 62, 69, 79, 100, 150])
