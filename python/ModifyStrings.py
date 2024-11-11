"""
Python - Modify Strings
Python has a set of built-in methods that you can use on strings.
"""
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

"""
Remove Whitespace
Whitespace is the space before and/or after the actual text, and very often you want to remove this space
"""
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

"""
String Concatenation
To concatenate, or combine, two strings you can use the + operator.

"""
a = "Hello"
b = "World"
c = a + b
print(c)
