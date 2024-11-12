"""
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, 

the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
"""

thislist = ["apple", "banana", "cherry"]
print(thislist)


#This will return the items from position 2 to 5.
#Remember that the first item is position 0,
#and note that the item in position 5 is NOT included
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


list1 = ["abc", 34, True, 40, "male"]
print(list1)
for x in list1:
  print (x)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) 


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
