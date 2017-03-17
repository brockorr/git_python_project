#!/usr/bin/python
''' This is my docstring
'''
# I did this a little differently, but we can still do the lesson.
# first import socket so we can deal with the IP address.
# Remember, socket a to n technically converts the ip address to a number, but it only
# Converts valid addresses, which is why it's valid to do this way.
import socket

def test_ipv4_address(ip_address):
    '''this is my IPV4 test function
    '''
    check = False
    try:
        socket.inet_aton(ip_address)
        check = True
    except socket.error:
        check = False
    return check

def convert_to_binary(ip_address):
    '''docstring
    '''
	# Split the IP address into a list
    ip_address = ip_address.split('.')
    # Create a binary list variable
    ip_address_binary = []
    for index, octet in enumerate(ip_address):
        ip_address_binary.append(format(int(ip_address[index]), '#010b'))
    # Return the list
    return ip_address_binary
    