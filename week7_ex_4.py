#!/usr/bin/python

# I'm supposed to be experimenting with globs, which is apparently going to make it
# easier to search through multiple files.

from glob import glob
from collections import defaultdict
import re

cdp_files = glob('class7/CDP_DATA/*_cdp.txt')
print cdp_files

print type(cdp_files)

hostname = r"Device ID: (.+)"
ip = r"IP address: (.+)"
platform = r"Platform: (.+?) (.+?) "
device_attributes = [('hostname', hostname), ('ip', ip), ('platform', platform)]
device_attributes_default_dictionary = defaultdict(list)
hostname_attributes_default_dictionary = defaultdict(list)

for index, filename in enumerate(cdp_files):
    cdp_file = open(filename, "rb")
    cdp_file = cdp_file.read()
    hostname_attributes_default_dictionary[filename].append(filename)
    for index2, value in device_attributes:
        hostname_attributes_default_dictionary[filename].append(re.findall(value, cdp_file))
        

for index, value in hostname_attributes_default_dictionary.iteritems():
    print value
    for ix, it in enumerate(value):
       if isinstance(it, list) == True:
            for jx, j in enumerate(it):
                print j


## I need to create an instance of a dictionary.
## Host([list of things])