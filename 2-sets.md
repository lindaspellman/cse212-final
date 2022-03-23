
# Introduction to Sets
## Characteristics of Sets
- don't care about order
- doesn't allow duplicate data, which means you can efficiently test the set on whether a certain piece of data is a member of the set
- easy to convert a list to a set, no raising errors, just filters the duplicates

## Uses
- Finding the unique values in a list.
- Providing quick access to unique results previously calculated. 
- Performing mathematical set operations such as an intersection (common values between two sets) and union (all values within two sets).

# Hashing

Hashing is the name of the technique used to add, remove, and efficiently test for membership in a set. 
- index(n) hashing function is not based on the order the value was added.

## Dealing with Index Conflicts

2 common ways to deal with conflicts
- open addressing
- chaining

# Sets in Python

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

# Example

# Problem to Solve

