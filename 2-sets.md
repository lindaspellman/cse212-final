# Introduction to Sets
## Basic Details
Sets don't allow duplicate data, which means that it is easy to convert a list to a set because duplicate values are simply filtered out, thereby raising no errors. Sets don't care about order either, which means that, when combined with a lack of duplicate data, it is highly efficient to test for a value's membership in the set.

## Uses of Sets
Sets can be used in several ways. First, they can be used to find unique values in a list. Second, in the case of a previous calculation, sets provide quick access to the given unique results. Third, sets can be used to perform mathematical set operations such as an intersection and union. Intersections refer to common values between two sets. Unions refer to all values within two sets.

## Hashing
Hashing is the name of the technique used to add, remove, and efficiently test for membership in a set. It is the process of translating a given key into a code. Adding values to a set via hashing ends in a set called a "sparse list." This means that, since sets don't care about order, the list can have gaps in its index. 
In order to place a value into a set, use this generic function:
```
index(n) = hash(n) % sparse_list_size.
```
The hash(n) represents what is called a hashing function. The hashing function will convert non-integers into integers so that the modulo operation can be performed. Python has a built-in hash function. The values returned by the hash function will vary everytime you run a Python script, but they will be consistent while you are running a script to completion. Not everything can be hashed. For example, a list in Python cannot be hashed. It is common to say that the index(n) is the hashing function for a set and that the values in a set have been hashed.

## Dealing with Index Conflicts

2 common ways to deal with conflicts
- open addressing
- chaining

## Sets in Python

Sets can be represented using curly braces, but if you're familiar with dictionaries or maps, you'll know that Python also represents those using curly braces. So, in order to differentiate sets from dictionaries, an empty set is indicated with the set() function.

``` python
empty_set = set()
```

Adding to a set:
``` python
my_set.add(value)
```

Removing from a set:
``` python
my_set.remove(value)
```

Checking for membership in a set:
``` python
if value in my_set:
```

Finding the size of a set:
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

## Example

## Problem to Solve

