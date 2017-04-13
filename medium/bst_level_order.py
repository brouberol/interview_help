# Given a binary search tree, print out the elements in level order.
# for example, for the tree 

#       8
#      /\
#     6  9
#    /\   \
#    5 7  11
#
#  It will print 8 6 9 5 7 11
#
#
#

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

    def level_order_traversal(self):
        node = self.root
        if not node:
            return []
        out = []
        queue = deque([node])
        while queue:
            node = queue.popleft()
            out.append(node.value)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return out
