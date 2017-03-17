#!/usr/bin/python
'''
b. Create a program that opens the 'sw1_cdp.txt' file and finds all of the remote:
>hostnames
>IP addresses
>platforms.  

Your output should look similar to the following:
remote_hosts: ['R1', 'R2', 'R3', 'R4', 'R5']
IPs: ['10.1.1.1', '10.1.1.2', '10.1.1.3', '10.1.1.4', '10.1.1.5']
platform: ['Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881', 'Cisco 881']

'''

# First things first, import the required modules, os for the files and re for regex

import os
import re
# I want to be able to add lists to dictionaries, so this is what the internet recco
from collections import defaultdict

'''
https://docs.python.org/2/library/collections.html#collections.defaultdict
example default dict
orig_dict = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
defaultdictionary = defaultdict(list)
for index, value in orig_dict:
        defaultdictionary[index].append(value)
'''
# next import the file using rb for windows compat. reasons.
cdp_file = open("class7/CDP_DATA/sw1_cdp.txt", "rb")
cdp_file = cdp_file.read()

# then declare your strings of what you actually want to search
hostname = r"Device ID: (.+)"
ip = r"IP address: (.+)"
platform = r"Platform: (.+?) (.+?) "

# Lets create a named list of what I want to look for, and slide those strings into it
device_attributes = [('hostname', hostname), ('ip', ip), ('platform', platform)]

# And now let's make a default dictionary
# default dictionaries are a subspecies of dictionary that has special modifications
# they allow us to add lists into dictionaries in a desireable way.
device_attributes_default_dictionary = defaultdict(list)

# Now let's iterate over the list
# I'm findall-ing the matches from before and adding them into a dictionary with 
# an understandable key, which results in a dictionary of lists.
print type(device_attributes)
for index, value in device_attributes:
    device_attributes_default_dictionary[index].append(re.findall(value, cdp_file))

for index, value in device_attributes_default_dictionary.iteritems():
    print value