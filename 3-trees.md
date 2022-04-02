# Introduction to Trees
Trees are a data structure that are similar to linked lists. They have pointers like linked lists do, but they are different in that they can be connected to many different nodes. 
There are four types of trees: 
- binary
- binary search
- balanced binary search trees
- non-binary trees

## Binary Trees
A binary tree is a tree that links to no more than two other nodes. The top node is called the root node. There is always only one root node. The nodes at the end of the tree are called leaf nodes. A parent node is a non-root node and non-leaf node, thereby lying somewhere within the tree. The nodes to the left and right of any parent node form a subtree, constituting child nodes. Child nodes are any nodes connected to a parent node. They can be leaf nodes but never the root node. It is common for child nodes to also point back up to the parent node.

## Binary Search Trees
A binary search tree is different from a binary tree because it follows rules that dictate how data is inserted into the tree. Data can only be placed into the BST after it has been compared withthe value of the parent node. Data that is less than the parent node is shunted to the left subtree, or else it goes to the right subtree. Duplicates have a choice of which side they are placed, in the case that duplicates are allowed. The comparison continues down the subtrees until an empty place is found for the data.

## Balanced Binary Search Trees
A balanced binary search tree is a BST whose subtree height are relatively equal. The number of nodes between the root and leaves determine the height of a tree.

## Non-binary Trees
Non-binary trees are similar to the aforementioned binary trees, except for a vital difference. Non-binary trees are able to have any number of child nodes attached to their parent nodes. This can make for very long and complicated subtrees.

## BST Operations
### Inserting into a BST
Insertion is a recursive operation where the subtrees are searched to find the next available place for the data to be inserted. Its performance equates to O(log n).

In Python, 
### Traversing a BST
Traversing a BST requires two different functions: traverse_forward and traverse_reverse. The former function travels the BST from smallest to largest values and performs at a speed of O(n). The latter travels the opposite way, from largest to smallest values, but also performs at O(n). 

### Other Important BST Operations
``` python
remove(value)
```

``` python
contains(value)
```

``` python
height(node)
```

``` python
size()
```

``` python
empty()
```
## Example
## Problem to Solve


[Solution](.py)
- [Return to Welcome Page](0-welcome.md)
