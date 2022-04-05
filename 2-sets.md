# Introduction to Sets
## Basic Details
Sets don't allow duplicate data, which means that it is easy to convert a list to a set because duplicate values are simply filtered out, thereby raising no errors. Sets don't care about order either, which means that, when combined with a lack of duplicate data, it is highly efficient to test for a value's membership in the set.

## Uses of Sets
Sets can be used in several ways. First, they can be used to find unique values in a list. Second, in the case of a previous calculation, sets provide quick access to the given unique results. Third, sets can be used to perform mathematical set operations such as an intersection and union. Intersections refer to common values between two sets. Unions refer to all values within two sets.

## Hashing
Hashing is the name of the technique used to add, remove, and efficiently test for membership in a set, giving us O(1) timing.. It is the process of translating a given key into a code. Adding values to a set via hashing ends in a set called a "sparse list." This means that, since sets don't care about order, the list can have gaps in its index. 
In order to place a value into a set, use this generic function, using a hashing function as a variable:
```
index(n) = hash(n) % sparse_list_size.
```
You can use Python's built-in hashing function. Hashing function converts non-integers into integers because the modulo operation can only be performed on integers. Not everything can be hashed, such as a list. The point of hashing with sets is to hash individual numbers and place them within sets, so it would not make sense to be able to hash a list. 

### How to Deal with Index Conflicts
There are two common ways to deal with conflicts
- open addressing
- chaining

Open addressing is used in the case that a value is sent to a certain index based on its hashing, but that index is already taken by a different value. Open addressing states that this value should be sent to the next available index. But if the new index is already filled as well as subsequent indexes, clusters of conflict will erupt until an empty index is found. 

Chaining, on the other hand, does not create clusters of conflict. Instead, it creates a list to which you can add new values, so that they all can co-exist in the same index. 

The problem with these options is that they dismantle our O(1) timing and create O(n) timing. The solution to this is to increase the size of the sparse list and re-index all the values.

## Sets in Python
Sets can be represented using curly braces, but if you're familiar with dictionaries or maps, you'll know that Python also represents those using curly braces. So, in order to differentiate sets from dictionaries, an empty set is indicated with the set() function. Set operations are very fast and efficient. 

``` python
empty_set = set()
```

Adding to a set is O(1).
``` python
my_set.add(value)
```

Removing from a set is O(1).
``` python
my_set.remove(value)
```

Checking for membership in a set is O(1).
``` python
if value in my_set:
```

Finding the size of a set is O(1).
``` python
length = len(my_set)
```

To find the intersection or union of two sets:
``` python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set3 = intersection(set1, set2)  # This will result in {4, 5}
set3 = set1 & set2               # Alternate way of writing an intersection

set4 = union(set1, set2)  # This will result in {1, 2, 3, 4, 5, 6, 7, 8}
set4 = set1 | set2        # Alternate way of writing a union
```

## Example: An Intersection and Union of Two Sets
Two classes are surveyed on their favorite colors. The two lists are combined into one unified set. Another set is taken of the colors that the two classes have in common, also known as the intersection.

``` python
class1 = {"blue", "red", "black", "green"}
class2 = {"blue", "black", "yellow", "purple", "orange"}

colors_in_common = intersection(class1, class2)
print(colors_in_common)

# This outputs: {'blue', 'black'}
```

## Problem to Solve: Favorite Cuisine
Three different were surveyed about the students' favorite cuisines.
They can be summarized as follows:

class1 = {"Italian", "Chinese", "American", "Mexican"}
class2 = {"American", "Japanese", "Korean", "Indian", "Thai"}
class3 = {"Mexican", "Brazilian", "American", "Chinese"}

Use the union set operator in order to create a fourth set combining each unique type of cuisine.

[Solution](set_prob_soln.py)
- [Return to Welcome Page](0-welcome.md)
