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