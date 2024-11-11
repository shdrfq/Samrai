"""Strings
Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

You can display a string literal with the print() function:"""
print("Hello")
print('Hello')

"""
Quotes Inside Quotes
You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

"""
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

"""
Assign String to a Variable
Assigning a string to a variable is done with the variable name followed by an equal sign and the string:
"""
a = "Hello"
print(a)

"""
Multiline Strings

You can assign a multiline string to a variable by using three quotes:

"""

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)
"""
Slicing
You can return a range of characters by using the slice syntax.

Specify the start index and the end index, separated by a colon, to return a part of the string.
"""
b = "Hello, World!"
print(b[2:5])  #output will be -->   llo

"""
Slice From the Start
By leaving out the start index, the range will start at the first character:
"""
b = "Hello, World!"
print(b[:5])

"""
Slice To the End
"""
b = "Hello, World!"
print(b[2:])

"""
Negative Indexing
Use negative indexes to start the slice from the end of the string:
"""
b = "Hello, World!"
print(b[-5:-2])