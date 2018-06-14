#!/usr/bin/python

import sys

'''
'''

def unique_char (s):
    unique = False

    a = {}
    for c in s:
        if c in a.keys():
            return False
        else:
            a[c] = 1
        
    return True

if __name__ == "__main__":
    s = "abcdefahijk"
    print unique_char(s)
