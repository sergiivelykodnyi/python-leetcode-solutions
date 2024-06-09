# 226. Invert Binary Tree

import unittest


class TreeNode:
    """Definition for a binary tree node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def list_to_tree(lst):
    """Convert list to binary tree."""
    if not lst:
        return None

    nodes = [None if val is None else TreeNode(val) for val in lst]
    childNodes = nodes[::-1]
    root = childNodes.pop()
    for node in nodes:
        if node:
            if childNodes:
                node.left = childNodes.pop()
            if childNodes:
                node.right = childNodes.pop()
    return root


def tree_to_list(root: TreeNode):
    """Convert binary tree to list."""
    if not root:
        return []

    nodes = [root]
    result = []

    while nodes:
        node = nodes.pop(0)

        if node:
            result.append(node.val)
            nodes.append(node.left)
            nodes.append(node.right)

    return result


# def invertTree(root: TreeNode) -> TreeNode:
#     """Invert binary tree recursively."""
#     if root:
#         # swap left and right children
#         root.left, root.right = root.right, root.left

#         # recursively call invertTree on left and right children
#         invertTree(root.left)
#         invertTree(root.right)

#     return root

# invert binary tree iteratively


def invert_tree(root:  TreeNode) -> TreeNode:
    """Invert binary tree iteratively."""
    if not root:
        return None

    children = [root.left, root.right]

    # swap left and right children
    root.left, root.right = root.right, root.left

    while children:
        child = children.pop()

        if child:
            # append left and right children to children list
            children.append(child.left)
            children.append(child.right)

            # swap left and right children
            child.left, child.right = child.right, child.left

    return root


class TestInvertTree(unittest.TestCase):
    def test_invert_tree(self):
        self.assertEqual(tree_to_list(invert_tree(
            list_to_tree([4, 2, 7, 1, 3, 6, 9]))), [4, 7, 2, 9, 6, 3, 1])
        self.assertEqual(tree_to_list(invert_tree(
            list_to_tree([1, 2, 3, 4, 5, 6, 7]))), [1, 3, 2, 7, 6, 5, 4])
        self.assertEqual(tree_to_list(
            invert_tree(list_to_tree([2, 1, 3]))), [2, 3, 1])
        self.assertEqual(tree_to_list(
            invert_tree(list_to_tree([1, 2]))), [1, 2])


if __name__ == '__main__':
    unittest.main()
