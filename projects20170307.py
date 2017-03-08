#!/usr/bin/python


''' below are lessons from week 6 of the python class.


1. Create a function that returns the multiplacaion of a product of three params: x,y,z
z should have a default value of 1.
'''

print("Project 1")
# A Call the function will all positional arguments
def funct_a(x,y,z=1):
	return x*y*z

# B Call the function will all named arguments
def funct_b(x,y,z):
	return x*y*z

# C call the function with a mix of positional and named arguments.
def funct_c(x,y,z):
	return x*y*z

# D call the function with only two arguemts and use the default value of z.
def funct_d(x,y,z=1):
	return x*y*z


print funct_a(1, 2, 3)
print funct_b(x=1,y=2,z=3)
print funct_c(1, 2, z=3)
print funct_d(1,2)

print("Project 2")
''' Write a function that converts a list to a dictionary where the index of the list is used as the key to the new dictionary. The function should return the new dictionary.

Notes: ways to findor iterateate over the length of a list.
1. len(list_var) -- this returns an int of the list.
2. for index, value in enumerate(list_var): print(index, value)
	Enumerate is an object that stores the index and the value of the index.

'''
# Declaring a list
gateway_router_attributes = ["model", "sn", "market_name", "city", "ip"]

# Convert the list into a dictionary

def transform_to_dictionary(a_list):
	# Create the dictionary
	dictionary = {}
	# Figure out how long the list is
	# len()
	# Then use a loop to iterate over the list and add the dictionary
	
	for index, value in enumerate(a_list):
		dictionary.update({value: ""})
	return dictionary

# Then call the function

converted_list = transform_to_dictionary(gateway_router_attributes)
print(converted_list)

print("###################")
''' And now I'm going to convert the ip address validation code into a function, take one variable (ip address) and return whether it's a valid IP - true or false


'''
# I did this a little differently, but we can still do the lesson.
# first import socket so we can deal with the IP address.
# Remember, socket a to n technically converts the ip address to a number, but it only
# Converts valid addresses, which is why it's valid to do this way.
import socket

def test_ipv4_address(ip):
	check = False
	try:
		socket.inet_aton(ip)
		check = True
	except:
		check = False

	return check

ip_address = "10.5.0.999"
print(test_ipv4_address(ip_address))

''' Now i'm supposed to call it from the python command prompt. 
First import the file with an import {filename} statement
Second call the function by typing {filename}.test_ipv4_address({ip_var})

Now im supposed to call it another way
First import the file with a from {filename} import {test_ipv4_address}

NOTE: This executes all the things in the main init section of the file before it loads
the funtion into itself.

Second, you can then call the function directly without using the module.
