#!/usr/bin/python

import sys

'''
'''

def replace_space (s, l):
    i = l-1

    space = 0
    for t in s[:l]:
        if t == ' ':
            space = space + 1

    j = l+(space*2)-1

    while i >= 0:
        if s[i] == ' ':
            s[j] = '0'
            s[j-1] = '2' 
            s[j-2] = '%' 
            j = j - 3
        else:
            s[j] = s[i]
            j = j - 1

        i = i - 1

if __name__ == "__main__":
    t = list("VAMSI IS A BOY              ")
    print t
    replace_space(t, 14)
    print t
