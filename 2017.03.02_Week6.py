#!/usr/bin/python

'''
WEEK 6
NOTES

Good Programming Laws:
Never repeat yourself. Use Functions

Preaching Code Re-Usability
- The main purpose behind using functions is for code reusability.
- You can re-use functions in multiple applications.
- It eliminates or reduces drift between your code. Never repeat

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
Docstrings can be quoted

Functins with Parameters

def a_sum(x, y):
	return x+y

a_sum(5,10)

this will return 15.
This tiny function will support strings and lists too because both support +.

By default, the parameters map by position, but when you call the function, you 
can explicitly name the parameters youre passing. You can also mix the positional
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
	# here, simple_func have its own namespace, so these x and y's are different
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

'''
Functions Part 2
Be careful when you're passing in dictionaries and lists and objects becasue
they can change in your function. However, strings and integers are immutable.


the naming standard for functions is the same as it is for variables.

When you import a python module, all executable statements are executed when its imprtd
functions are still executed when they are called.

Also, when you call a function in a module, you have to call it via [modulename].function. The module name is the filename minus py. You can also add it directly to your programs namespace, but you have to type: from import ____ in order for it to work (keyword from)

'''
def f1(a_list):
	a_list.append("whatever")
a = range(10)
f1(a)
print(a)
# Here, the list A is modified by the function call. 
# a_list is a local parameter to f1.
# a is declared in memory, but when you pass the list into the function, it points
# to the actual a object in memory, so you can modify the object inside a function

def f2(a_list):
	# At this moment, a_list is a reference to the b object in memory
	a_list = []
	# Now, the a_list list points to its own object in memory.
	a_list.append('something')
	# This appends something to the blank a_list. 
	print(a_list)

b = range(10)
f2(b)
print(b)

print("################################################")

''' PROJECT 4
Create a function using your dotted decimal to binary conversion code from Class 3
In the function, do not prompt for input and do not print for standard output.
the function should take one variable ip_address and return the IP address in dotted binary format always padded to eight binary digits.

Notes on padding
The formatting specification mini language tells python how to format something.
binary variables are actually specially formatted strings wit 0b appended to the front of them. the #010b tells python to format the string as a binary that is 10 characters long. We need 8 digits, but it's 10 characters because the first two are taken up by 0b
'''

def convert_to_binary(ip_address):
	# Split the IP address into a list
	ip_address = ip_address.split('.')
	# Create a binary list variable
	ip_address_binary = []
	for index, octet in enumerate(ip_address): 
		ip_address_binary.append(format(int(ip_address[index]), '#010b'))
	# Return the list
	return ip_address_binary

ip_address = "10.5.0.1"

converted_address = convert_to_binary(ip_address)
print(converted_address)

	
