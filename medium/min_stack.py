# Implement a data structure that supports the native operations of stack, 
# push and pop, but also allow you to find the minimum in O(1) time.

# Solution is to under the hood maintain 2 stacks, one is the actual stack, and
# the other keeps the current minimum, and when the current minimum is popped
# off the stack, pop it off the stack

class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def __repr__(self):
        return "<{} min={}>".format(self.__class__.__name__, self.min)

    def push(self, value):
        self.stack.append(value)
        if not self.mins or value < self.mins[-1]:
            self.mins.append(value)

    def pop(self):
        val = self.stack.pop()
        if val == self.mins[-1]:
            self.mins.pop()
        return val

    @property
    def min(self):
        if self.mins:
            return self.mins[-1]
