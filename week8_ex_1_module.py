#!/usr/bin/python
def test_ipv4_address(ip_address, ip_library):
    '''this is my IPV4 test function
    '''
    check = False
    if ip_address in ip_library:
        if ip_library[ip_address] is True:
            check = True
        else:
            check = False
    else:
        check = False
    return check

def list_valid_ipv4_addresses(ip_library):
    '''this spits out all the valid ip addresses in the list.
    '''
    true_ip_list = []
    for item in list(ip_library.keys()):
        if ip_library[item] is True:
           true_ip_list.append(item)
    return true_ip_list
    

if __name__ == "__main__":
    ''' this part will be executed when the file is run

    '''
    test_ip_addresses = {
        '192.168.1' : False,
        '10.1.1.' : False,
        '10.1.1.x' : False,
        '0.77.22.19' : False,
        '-1.88.99.17' : False,
        '241.17.17.9' : False,
        '127.0.0.1' : False,
        '169.254.1.9' : False,
        '192.256.7.7' : False,
        '192.168.-1.7' : False,
        '10.1.1.256' : False,
        '1.1.1.1' : True,
        '223.255.255.255' : True,
        '223.0.0.0' : True,
        '10.200.255.1' : True,
        '192.168.17.1' : True
    }
    ip_address = str(raw_input("Enter the IP Address: "))
    print test_ipv4_address(ip_address, test_ip_addresses)
    print list_valid_ipv4_addresses(test_ip_addresses)