#!/usr/bin/python

import sys

from collections import defaultdict

'''
'''

def stairs (num_steps, d):
    
    if num_steps < 0:
        return 0
    elif num_steps == 0:
        return 1
    elif num_steps not in d:
        d[num_steps] = stairs(num_steps-1, d) + stairs(num_steps-2, d) + stairs(num_steps-3, d)

    return d[num_steps]
     

if __name__ == "__main__":
    d = defaultdict(dict)
    print stairs(4, d)
