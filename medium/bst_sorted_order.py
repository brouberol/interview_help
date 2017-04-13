# Given a binary search tree, print out the elements in sorted order.

from collections import deque


class Node:

    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __repr__(self):
        return '<Node {} left={} right={}>'.format(
            self.value,
            self.left.value if self.left else 'None',
            self.right.value if self.right else 'None')


class BST:

    def __init__(self):
        self.root = None

    @classmethod
    def from_list(cls, l):
        tree = BST()
        tree.root = Node(l[0])
        for i in l[1:]:
            node = tree.root
            while True:
                if i <= node.value:
                    if node.left:
                        node = node.left
                    else:
                        node.left = Node(i)
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = Node(i)
                        break
        return tree

    def _sorted_order_traversal(self, node=None):
        if not node:
            return []
        out = []
        out.extend(self._sorted_order_traversal(node.left))
        out.append(node.value)
        out.extend(self._sorted_order_traversal(node.right))
        return out

    def sorted_order_traversal(self):
        return self._sorted_order_traversal(self.root)
