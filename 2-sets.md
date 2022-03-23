
# Introduction to Sets
## Characteristics
Sets:
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

# Dealing with Conflicts

2 common ways to deal with conflicts
- open addressing
- chaining

# Sets in Python

Sets can be represented using curly braces, but if you're familiar with dictionaries or maps, you'll know that Python also represents those using curly braces. So, in order to differentiate sets from dictionaries, an empty set is indicated with set() function.

``` python
empty_set = set()
```



# Example

# Problem to Solve
