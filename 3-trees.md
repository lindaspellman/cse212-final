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
- Traverse_forward
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
- Traverse_reverse
``` python
def __reversed__(self):
	"""
	Perform a formward traversal (in order traversal) starting from 
	the root of the BST.  This function is called when a the 
	reversed function is called and is frequently used with a for
	loop.

	for value in reversed(my_bst):
	    print(value)

	"""        
	yield from self._traverse_backward(self.root)  # Start at the root
	
def _traverse_backward(self, node):
	"""
	Does a backwards traversal (reverse in-order traversal) through the 
	BST.  If the node that we are given (which is the current
	sub-tree) exists, then we will keep traversing on the right
	side (thus getting the larger numbers first), then we will 
	provide the data in the current node, and finally we will 
	traverse on the left side (thus getting the smaller numbers last).

	This function is intended to be called the first time by 
	the __reversed__ function.        
	"""
	if node is not None:
	    yield from self._traverse_backward(node.right)
	    yield node.data
	    yield from self._traverse_backward(node.left)
```

### Other Important BST Operations
#### Testing for Membership
Here is an example of how to test for membership in a BST. 
``` python
def __contains__(self, data):
        """ 
        Checks if data is in the BST.  This function
        supports the ability to use the 'in' keyword:

        if 5 in my_bst:
            ("5 is in the bst")

        """
        return self._contains(data, self.root)  # Start at the root

def _contains(self, data, node):
        """
        This function will search for a node that contains
        'data'.  The current sub-tree being search is 
        represented by 'node'.  This function is intended
        to be called the first time by the __contains__ function.
        """
        if data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found the bottom of the tree
                return False 
            else:
                # Need to keep looking.  Call _contains
                # recursively on the left sub-tree.
                return self._contains(data, node.left)
        
        elif data == node.data:
            return True 
        
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found the bottom of the tree
                return False
            else:
                # Need to keep looking.  Call _contains
                # recursively on the right sub-tree.
                return self._contains(data, node.right)
```

#### Finding the Height
Here is an example of how to use recursion in order to find the height of a BST. 
``` python
def get_height(self):
        """
        Determine the height of the BST.  Note that an empty tree
        will have a height of 0 and a tree with one item (root) will
        have a height of 1.
        
        If the tree is empty, then return 0.  Otherwise, call 
        _get_height on the root which will recursively determine the 
        height of the tree.
        """
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)  # Start at the root

def _get_height(self, node):
        """
        Determine the height of the BST.  The height of a sub-tree 
        (represented by 'node') is 1 plus the height of either the 
        left sub-tree or the right sub-tree (whichever one is bigger).

        This function intended to be called the first time by 
        get_height.
        """
        if node is None:
            return 0
        else:
            left_height = self._get_height(node.left)
            right_height = self._get_height(node.right)
            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1
```
#### Finding the Size
The size() and empty() operations can be conducted using the same code.
``` python
def size(node):
    if node is None:
        return 0
    else:
        return (size(node.left)+ 1 + size(node.right))
```
## Example

## Problem to Solve
Use this base code in order to write code for how to remove a node from A BST.
``` python
# Helper function to find minimum value node in the subtree rooted at `curr`
def getMinimumKey(curr):
    while curr.left:
        curr = curr.left
    return curr

# Function to delete a node from a BST
def remove_node(root, key):
 
    # pointer to store the parent of the current node
    parent = None
 
    # start with the root node
    curr = root
 
    # search key in the BST and set its parent pointer
    while curr and curr.data != key:
 
        # update the parent to the current node
        parent = curr
 
        # if the given key is less than the current node, go to the left subtree;
        # otherwise, go to the right subtree
        if key < curr.data:
            ### CODE HERE
        else:
            ### CODE HERE
 
    # return if the key is not found in the tree
    if curr is None:
        return root
 
    # Case 1: node to be deleted has no children, i.e., it is a leaf node
    if curr.left is None and curr.right is None:
 
        # if the node to be deleted is not a root node, then set its
        # parent left/right child to None
        if curr != root:
            ### CODE HERE
 
        # if the tree has only a root node, set it to None
        else:
            root = None
 
    # Case 2: node to be deleted has two children
    elif curr.left and curr.right:
 
        # find its inorder successor node
        successor = getMinimumKey(curr.right)
 
        # store successor value
        val = successor.data
 
        # recursively delete the successor. Note that the successor
        # will have at most one child (right child)
        remove_node(root, successor.data)
 
        # copy value of the successor to the current node
        curr.data = val
 
    # Case 3: node to be deleted has only one child
    else:
 
        # choose a child node
        if curr.left:
            child = curr.left
        else:
            child = curr.right
 
        # if the node to be deleted is not a root node, set its parent
        # to its child
        if curr != root:
            ### CODE HERE
 
        # if the node to be deleted is a root node, then set the root to the child
        else:
            root = child
 
    return root
```
[Solution](trees_prob_soln.py)
- [Return to Welcome Page](0-welcome.md)
