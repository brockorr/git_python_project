#!/usr/bin/python

'''
write a program that:
0. Re-use the functions created in excercises 3 and 4
1. Prompts a user for an ip address
2. Checks to see if the address is valid
3. Converts the IP address to binary (dotted decimal format)
'''

# 0. Re-use the functions created in excercises 3 and 4
import week6_exercise5_modules

ip = raw_input("Enter an IP Address:  ")

print week6_exercise5_modules.test_ipv4_address(ip)
print week6_exercise5_modules.convert_to_binary(ip)
