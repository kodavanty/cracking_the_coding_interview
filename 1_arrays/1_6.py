#!/usr/bin/python

import sys

'''
'''

def rotate_array_90 (a):

    print a

    # For each layer
    for layer in range(len(a)/2):
        first = layer
        last  = len(a)-layer-1
        for offset in xrange(0, last-first):
            #print layer, first, last, offset
            # copy top to temp
            temp = a[first][offset]
            # copy left to top
            a[first][offset] = a[last-offset][first]
            # copy bottom to left
            a[last-offset][first] = a[last][last-offset]
            # copy right to bottom
            a[last][last-offset] = a[first+offset][last]
            # copy temp to right
            a[first+offset][last] = temp

    print a

if __name__ == "__main__":
    w, h = 4, 4
    a = [[i for i in range(w)] for j in range(h)] 
    rotate_array_90(a)
