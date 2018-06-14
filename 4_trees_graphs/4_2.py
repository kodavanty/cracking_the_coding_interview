#!/usr/bin/python

import sys

from graph import Graph
from collections import deque

'''
'''

def path_exists (graph, source, dest):
    s = graph.get_vertex(source)

    l = deque([s])

    while len(l):
        v = l.popleft()
        for n in v.get_edges():
            if n.get_key() == dest:
                return "TRUE"
            else:
                if n not in l:
                    l.append(n)

    return "FALSE"

if __name__ == "__main__":
    g = {
        1: {2: 1, 3: 1, 5: 1},
        2: {3: 1, 4: 1},
        3: {},
        4: {5: 1},
        5: {1: 1},
    }

    graph = Graph(g)
    graph.show()
    print path_exists(graph, 3, 5)
