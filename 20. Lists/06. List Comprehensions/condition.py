# The condition is like a filter that only accepts the items
# that valuate to True.

# Only accept items that are not "apple":
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]

# The condition if x != "apple"  will return True for all elements
# other than "apple", making the new list contain all fruits except "apple".

# The condition is optional and can be omitted:

# With no if statement:
newlist = [x for x in fruits]