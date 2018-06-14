#!/usr/bin/python

import sys

'''
'''

def set_char (array, index, char, count):
    array[index] = char
    index = index + 1

    for c in str(count):
        array[index] = c
        index = index + 1

    return index

def string_compression (s):

    t = s[:]

    print s

    char = {}
    for c in s:
        if c in char.keys():
            char[c] = char[c] + 1
        else:
            char[c] = 1

    comp_count = len(char.keys())*2

    if comp_count >= len(s):
        return s

    prev = s[0]
    count = 1
    i = 0
    for c in s[1:]:
        if c != prev:
            i = set_char(t, i, prev, count)
            count = 1
            prev = c
        else:
            count = count + 1

    set_char(t, i, prev, count)

    print t[:comp_count]

if __name__ == "__main__":
    string_compression(list("aaaaaaaabbcdeeeeeeeeeeeff"))
