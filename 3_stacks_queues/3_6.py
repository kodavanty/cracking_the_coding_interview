#!/usr/bin/python

import sys

'''
'''
class SortedStack:
    def __init__ (self):
        self.stack = []
        self.temp  = []

    def push (self, val):
        if len(self.stack) == 0:
            self.stack.append(val)
            return

        if val > self.stack[len(self.stack)-1]:
            self.stack.append(val)
        else:
            while len(self.stack):
                if val < self.stack[len(self.stack)-1]:
                    self.temp.append(self.stack.pop())
                else:
                    break

            self.stack.append(val)
            while len(self.temp):
                self.stack.append(self.temp.pop())

    def pop (self):
        return self.stack.pop()

def sort_stack ():
    s = SortedStack()
    s.push(10)
    s.push(20)
    s.push(15)
    s.push(40)
    s.push(5)

    print s.pop(), s.pop(), s.pop()
    print s.stack

if __name__ == "__main__":
    sort_stack()
