"""
Dictionary
Dictionaries are used to store data values in key:value pairs.

A dictionary is a collection which is ordered*, changeable and do not allow duplicates."""


dictionary_1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(dictionary_1)

"""
Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
"""

dictionary_2 = {
  "brand": "Ford",
  "model": "Mustang-1",
  "model": "Mustang-2",
  "year": 1964
}
print(dictionary_2["brand"])
print(dictionary_2["model"])

print("===================")
"""
Loop Through a Dictionary
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
  print(x)
print("========value===========")
"""
Loop shahow value a Dictionary
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
  print(x)

print("======show keys=============")
"""
Loop Through a Dictionary
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
  print(x)

print("======show value=============")
"""
Loop Through a Dictionary
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
  print(thisdict[x])

print("======show item=============")
"""
Example
Loop through both keys and values, by using the items() method:
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

print("======COPY DICTIONALARY============")
"""
Example
Loop through both keys and values, by using the items() method:
"""
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)


# Copy a Dictionary
# You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.
# There are ways to make a copy, one way is to use the built-in Dictionary method copy().
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
for x in mydict.values():
  print(x)  

for x in mydict.items():
  print(x)   

# second way to make copy of existing available dictionary 
thisdict = {
  "brand": "Ford",
  "model": "Mustang1",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)  