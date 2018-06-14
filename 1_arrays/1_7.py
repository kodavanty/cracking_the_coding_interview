#!/usr/bin/python

import sys

'''
'''

def zero_array (a):
    rows = []
    cols = []

    for i in range(len(a)):
        for j in range(len(a)):
            if a[i][j] == 0:
                if i not in rows:
                    rows.append(i)
                if j not in cols:
                    cols.append(j)
    
    for i in range(len(a)):
        for j in range(len(a)):
            if i in rows or j in cols:
                a[i][j] = 0

    for i in range(len(a)):
        print a[i]

if __name__ == "__main__":
    a = [[0, 1, 0, 1, 1, 1],
         [1, 1, 0, 1, 1, 1],
         [0, 1, 0, 1, 0, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1],
         [1, 1, 1, 1, 1, 1]]
    for i in range(len(a)):
        print a[i]
    print 

    zero_array (a)
