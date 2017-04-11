#!\usr\bin\python
'''
classes and objects.
A class is a blueprint regarding assigning variables and assigning functions. it specifies how to create some thing. An instance of this class is an object.

def create_network_device(ip, username, password):
        net dev = {}
        det_dev['ip'] = ip
        net_dev['username'] = username
        net_dev['password'] = password
        return net_dev
rtr1 = create_network_device('1.1.1.1', 'ktb', 'pass')
print rtr1
>> returns a dictionary of rtr1 attributes

rtr2 = create_network_device('12.1.1.1', 'ktb', 'pass')

NOW LETS CREATE THE SAME THING BY USING CLASSES AND OBJECTS
Note the CamelCase capitalization.
Inheritance: if you're not inheriting anything from another object or base class, you need to do ClassName(object). 

New Style Classes - in 2.2+
    class NetworkDevice(object):
Old Style CLasses - old
    class NetworkDevice
class NetworkDevice(object):
        pass

rtr3 = NetworkDevice()
rtr3.ip = "1.2.2.1"


class NetworkDevice(object):
   #NOTE THIS IS NOT A FUNCTION, this is a method because its in a class.
   # __init__ is a special method taht is automatically invoked when you 
   # create an instance of the object.
   # convention: when you are passing variables into a method, you need to 
   declar self as a variable.
    def __init__(self, ip, username, password)
        self.ip = ip
        self.username = username
        self.password = password


rtr3 = NetworkDevice('10.2.2.2', 'ktb', 'some_pass')

