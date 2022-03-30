# Introduction
Trees are a data structure that are similar to linked lists. They have pointers like linked lists do, but they are different in that they can be connected to many different nodes. 
There are three types of trees: 
- binary
- binary search
- balanced binary search trees

## Binary Trees
A binary tree is a tree that links to no more than two other nodes. The top node is called the root node. There is always only one root node. The nodes at the end of the tree are called leaf nodes. A parent node is a non-root node and non-leaf node, thereby lying somewhere within the tree. The nodes to the left and right of any parent node form a subtree, constituting child nodes. Child nodes are any nodes connected to a parent node. They can be leaf nodes but never the root node. It is common for child nodes to also point back up to the parent node.

## Binary Search Trees
A binary search tree is different from a binary tree because it follows rules that dictate how data is inserted into the tree. Data can only be placed into the BST after it has been compared withthe value of the parent node. Data that is less than the parent node is shunted to the left subtree, or else it goes to the right subtree. Duplicates have a choice of which side they are placed, in the case that duplicates are allowed. The comparison continues down the subtrees until an empty place is found for the data.

## Balanced Binary Search Trees
A balanced binary search tree is a BST whose subtree height are relatively equal. The number of nodes between the root and leaves determine the height of a tree.

## BST Operations
### Inserting into a BST
Insertion is a recursive operation, meaning that you must write a base case and a smaller problem, which are needed to end the base case properly.

In Python, 
### Traversing a BST
## BST in Python
## Example
## Problem to Solve
