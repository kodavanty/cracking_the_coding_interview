#!/usr/bin/python

import sys

'''
'''
ENQUEUE = 1
DEQUEUE = 2
NONE    = 3

class Q2Stacks:
    def __init__ (self):
        self.stack1 = []
        self.stack2 = []
        self.prev_op = NONE
        self.current_stack = self.stack1

    def swap_stack (self):
        other_stack = self.stack1 if self.current_stack is self.stack2 else self.stack2

        while len(self.current_stack):
            other_stack.append(self.current_stack.pop())

        self.current_stack = other_stack
            
    def enqueue (self, val):
        if self.prev_op != ENQUEUE:
            self.swap_stack()
            self.prev_op = ENQUEUE

        self.current_stack.append(val)  

    def dequeue (self):
        if self.prev_op != DEQUEUE:
            self.swap_stack()
            self.prev_op = DEQUEUE

        return self.current_stack.pop() if len(self.current_stack) else "EMPTY"

def queue_two_stacks ():
    q = Q2Stacks()
    q.enqueue(10)
    q.enqueue(20)
    print q.dequeue()
    q.enqueue(15)
    q.enqueue(40)
    print q.dequeue()
    print q.dequeue()
    print q.dequeue()

if __name__ == "__main__":
    queue_two_stacks()
