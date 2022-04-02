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
Binary search trees are not naturally built into Python, so they must be coded in as a BST class. Each node of the BST is coded as a nested Node class. The Node class contains three variables: data (the value), left (pointer to the left node), and right (pointer to the right node).

The BST class includes major functions for inserting values and traversing the tree, shown below.

### Inserting into a BST
Insertion is a recursive operation where the subtrees are searched to find the next available place for the data to be inserted. Its performance equates to O(log n).

``` python
def insert(self, data):
	"""
	Insert 'data' into the BST.  If the BST
	is empty, then set the root equal to the new 
	node.  Otherwise, use _insert to recursively
	find the location to insert.
	"""
	if self.root is None:
		self.root = BST.Node(data)
	else:
		self._insert(data, self.root)  # Start at the root

def _insert(self, data, node):
	"""
	This function will look for a place to insert a node
	with 'data' inside of it.  The current subtree is
	represented by 'node'.  This function is intended to be
	called the first time by the insert function.
	"""
	if data < node.data:
		# The data belongs on the left side.
		if node.left is None:
			# We found an empty spot
			node.left = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the left subtree.
			self._insert(data, node.left)
	elif data >= node.data:
		# The data belongs on the right side.
		if node.right is None:
			# We found an empty spot
			node.right = BST.Node(data)
		else:
			# Need to keep looking.  Call _insert
			# recursively on the right subtree.
			self._insert(data, node.right)
``` 
### Traversing a BST
Traversing a BST requires two different functions: traverse_forward and traverse_reverse. The former function travels the BST from smallest to largest values and performs at a speed of O(n). The latter travels the opposite way, from largest to smallest values, but also performs at O(n). 

``` python
def __iter__(self):
	"""
    Perform a forward traversal (in order traversal) starting from 
    the root of the BST.  This is called a generator function.
    This function is called when a loop	is performed:

	for value in my_bst:
		print(value)

	"""
	yield from self._traverse_forward(self.root)  # Start at the root

def _traverse_forward(self, node):
	"""
	Does a forward traversal (in-order traversal) through the 
	BST.  If the node that we are given (which is the current
	subtree) exists, then we will keep traversing on the left
	side (thus getting the smaller numbers first), then we will 
	provide the data in the current node, and finally we will 
	traverse on the right side (thus getting the larger numbers last).

	The use of the 'yield' will allow this function to support loops
	like:

	for value in my_bst:
		print(value)

    The keyword 'yield' will return the value for the 'for' loop to
    use.  When the 'for' loop wants to get the next value, the code in
    this function will start back up where the last 'yield' returned a 
    value.  The keyword 'yield from' is used when our generator function
    needs to call another function for which a `yield` will be called.  
    In other words, the `yield` is delegated by the generator function
    to another function.

	This function is intended to be called the first time by 
	the __iter__ function.
	"""
	if node is not None:
		yield from self._traverse_forward(node.left)
		yield node.data
		yield from self._traverse_forward(node.right)
```

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
