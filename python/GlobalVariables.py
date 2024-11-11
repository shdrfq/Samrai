"""
Global Variables
Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

Global variables can be used by everyone, both inside of functions and outside.
"""

# Create a variable outside of a function, and use it inside the function

x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()


"""
Example
Create a variable inside a function, with the same name as the global variable

"""

z = "awesome"
def myfunc():
  z = "fantastic"
  print("Python is " + z)

myfunc()

print("Python is " + z)

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

"""

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

"""
If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

Example
Create a variable inside a function, with the same name as the global variable

"""
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

"""
The global Keyword
Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

Example
If you use the global keyword, the variable belongs to the global scope:

"""
def myfunc():
  global x
  x = "local but declare as global keyword"

myfunc()

print("variable  is " + x)
