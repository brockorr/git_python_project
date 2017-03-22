#!/usr/bin/python

'''
Open this file and extract the interface, IP address, area, type, cost, hello timer, and dead timer.  Use regular expressions to accomplish your extraction.

Your output should look similar to the following:

Int:        GigabitEthernet0/1
IP:        172.16.13.150/29
Area:    30395
Type:    BROADCAST
Cost:    1
Hello:   10
Dead:   40
'''


# First things first, import the required modules, os for the files and re for regex

import os
import re
# I want to be able to add lists to dictionaries, so this is what the internet recco
from collections import defaultdict

# next import the file using rb for windows compat. reasons.
ospf_file = open("class7/OSPF_DATA/ospf_data.txt", "rb")
ospf_file = ospf_file.read()

# and now lets play with regex. I want to find
# the interface, which is a line that does
# not begin with one or more spaces (the PLUS SIGN IS CRITICAL)
interface = r"(^[^\s]+)"
attributes = []
attributes.extend(re.findall(interface, ospf_file, re.MULTILINE))
# re.findall() returns a list. 
# if I used the .append METHOD then it would append a list to an empty list
# which is a list inside of a list [[list]], so I use extend, which extends
print attributes
for i in attributes:
    print i

ospf_file.readline()

# extract the interface name and description
