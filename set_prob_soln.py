# Three different were surveyed about the students' favorite cuisines.
# They can be summarized as follows:

class1 = {"Italian", "Chinese", "American", "Mexican"}
class2 = {"American", "Japanese", "Korean", "Indian", "Thai"}
class3 = {"Mexican", "Brazilian", "American", "Chinese"}

# Use the union set operator in order to create a fourth set combining each unique type of cuisine.

cuisines = class1 | class2 | class3
print(cuisines)
# Output: {'Chinese', 'Mexican', 'Italian', 'Indian', 'Korean', 'Thai', 'Japanese', 'Brazilian', 'American'}