# You can specify a range of indexes by specifying where to start
# and where to end the range.

# When specifying a range, the return value will be a new list with the
# specified items.

# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

# Note: The search will start at index 2 (included) and end at index 5
# (not included).

# Remember that the first item has index 0.

# By leaving out the start value, the range will start at the first item:

# This example returns the items from the beginning to,
# but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# By leaving out the end value, the range will go on to the end of the list:

# This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])