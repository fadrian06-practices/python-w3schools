# The iterable can be any iterable object, like a list, tuple, set etc.

# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]

# Same example, but with a condition:

# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
