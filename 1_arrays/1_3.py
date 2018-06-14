#!/usr/bin/python

import sys

'''
'''

def is_permutation_of_other (s1, s2):
    s3 = sorted(s1)
    s4 = sorted(s2)

    if s3 == s4:
        return True
    return False

if __name__ == "__main__":
    s1 = "abcdefg"
    s2 = "gfedcba"
    print is_permutation_of_other(s1, s2)
