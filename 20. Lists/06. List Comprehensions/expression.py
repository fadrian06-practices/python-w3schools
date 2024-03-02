# The expression is the current item in the iteration,
# but it is also the outcome, which you can manipulate before
# it ends up like a list item in the new list:

# Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]

# You can set the outcome to whatever you like:

# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]

# The expression can also contain conditions,
# not like a filter, but as a way to manipulate the outcome:

# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]

# The expression in the example above says:

# "Return the item if it is not banana, if it is banana return orange".