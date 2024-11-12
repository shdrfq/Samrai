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


thislist2 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
thislist2.append("shahid")
thislist2.insert(1, "javed")
thislist3 = ["1", "2", "3"]

thislist2.extend(thislist3)
print(thislist2)

"""
Add Any Iterable
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
"""

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
"""
Loop Through a List
You can loop through the list items by using a for loop:
"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)

  """
  Loop Through the Index Numbers
You can also loop through the list items by referring to their index number.

Use the range() and len() functions to create a suitable iterable.
  
  """
thislist = ["apple", "banana", "cherry"]
print(f"length of this list is  = {len(thislist)}")

for i in range(len(thislist)):
    print(thislist[i])

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)