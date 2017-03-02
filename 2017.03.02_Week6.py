#!/usr/bin/python

'''
WEEK 6
NOTES

Good Programming Laws:
Never repeat yourself. Use Function

Preaching Code Re-Usability
- The main purpose behind using functions is for code reusability.
- You can re-use functions in multiple applications.
- It Eliminates or reduces drift between your code. Never repeat

FUNCTIONS - All lowercase with underscores

def fun_cti_on():
	print(this is a function)
	return True
fun_ction()
a = fun_cti_on()
In python, when a function is called, it executes whatever is in the function. If nothing is returned from the function into the normal program, then it returns a NoneType.

NOTE ON DOCSTRINGS:
if you add a docstring to the function, you can type help(fun_cti_on) in the python
cli and it will show you the contents of the docstring.
Docstrings can be quoted with "" or ''

Functins with Parameters

def a_sum(x, y):
	return x+y

a_sum(5,10)

this will return 15.
This tiny function will support strings and lists too because both support +.

By default, the parameters map by position, but when you call the function, you 
can explicitly name the parameters you're passing. You can also mix the positional
and named arguments, but the positional arguments have to come first.

a_sum(y=20, x=10)
a_sum(40, z=20, y=10)

You can also in a function, define a default value. THis is a great way to
retroactively go back and add a default parameter.
def a_sum(x, y, z=100):
	return x+y+z

a_sum(2, 3)
returns: 105.

PYTHON NAMESPACE
The python Namespace in respect to functions.

Example:
'''
x = 10
y = 20
z = 30

def simple_func():
	x=100
	y=200
	print x
	print y
	print z
	# here, simple_func have it's own namespace, so these x and y's are different
	# than the ones in the main program. They're local to this function.
simple_func()
print(x)
print(y)
print(z)


# you'll note that z is not defined in simple_func(). When a variable is called in
# a namespace like this, pythonfirst tries to resolve the name in the local namesp.
# If itsnot defined in the local namespace, it goes back and looks at the module ns.
# and by "module" he means just a python file.
'''
once you exit out of the function the variables inside the function are destroyed.

'''
#Second  Example:
x = 10
y = 20
z = 30

def simple_func():
	def simple_func2():
		x = 1000
		print(x)
		print(y)
		print(z)
	x=100
	y=200
	
	print x
	print y
	print z

	simple_func2()

simple_func()
print(x)
print(y)
print(z)

# Here we have a nested function. when simple_func2() gets called, y is not defined
# locally, so it looks back to simple_func(). Z isnt in the local function or 
# the outer function, so it reverts back to the main module.
# the variables you define inside a function, they dont exist outside it, but 
# if the function calls a variable it doesnt have, it'll go hunting for it
# until it ends back up at the module leve.

# next example:
