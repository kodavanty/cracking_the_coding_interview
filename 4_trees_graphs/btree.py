from collections import deque

class BTreeNode:
    def __init__ (self, val):
        self.val = val
        self.l = None
        self.r = None
        self.p = None

class BTree:
    def __init__ (self, head):
        self.head = head

    def show (self):
        nodes = deque([self.head])
        count = 1
        level = 0
        
        while len(nodes):
            level = level + 1
            count = len(nodes)
            print "\nLevel %u (%u): " % (level, count),

            while count:
                n = nodes.popleft()
                pval = 0 if n.p is None else n.p.val
                print "%u[%u]" % (n.val, pval),

                if n.l is not None:
                    nodes.append(n.l)
                if n.r is not None:
                    nodes.append(n.r)

                count = count - 1

        print


