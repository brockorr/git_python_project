#!/usr/bin/python
'''
 a. Create a program that opens the 'r1_cdp.txt' file and using regular expressions extracts the remote hostname, remote IP address, model, vendor, and device_type.
 Device ID:
 IP Address:
 Platform:
 by: cisco systems
 Capabilities: 


 '''
import os
import re

cdp_file = open("class7/CDP_DATA/r1_cdp.txt", "rb")
cdp_file = cdp_file.read()
 
cdp_vendor_model = re.search(r"Platform: (.+?) (.+?) ", cdp_file)
cdp_capabilities = re.search(r"Capabilities: (.+?) (.+?) ", cdp_file)
cdp_remote_hostname = re.search(r"Device ID: (.+)", cdp_file)
cdp_remote_ip = re.search(r"IP address: (.+)", cdp_file)

print cdp_vendor_model.group(0)
print cdp_vendor_model.group(1)
print cdp_vendor_model.group(2)
print cdp_capabilities.group(0)
print cdp_capabilities.group(1)
print cdp_capabilities.group(2)
print cdp_remote_hostname.group(0)
print cdp_remote_hostname.group(1)
print cdp_remote_ip.group(0)
print cdp_remote_ip.group(1)