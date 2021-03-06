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

______________________________

Classes and objects - Part 

# The first parameter in an init class is always self referential, regardless of what it is called... but you should really call it self. Those the rules.
# Python automatically associated with this first variable name, the acutal object itself
    def __init__(self, ip, username, password) <--- (These, are, parameters).
        self.ip = ip <--- self.ip is the attribute, IP is the parameter)
        self.username = username
        self.password = password
    def a_product(self)


ATTRIBUTES belong to objects. class.attribute
PARAMETERS are the names of the variables that are passed in.
ARGUMENTS are what you pass inot a class when you are creating an object.  


rtr3 = NetworkDevice('10.2.2.2', 'ktb', 'some_pass') <---- ('these', 'are', 'arguments')



INHERITANCE

You could create a class that is based on a previous class.

class SomeClas
    __init___(self, x, y)
    self.x = x
    self.y = 7
    def a_sum(self)



class NewClass(SomeClass):
    def __init__(self, x, y, z):
        self.x = x
        self.y = i
        self.z = z
        SomeClass.__init__(self, x, y)
b = NewClass(8,9)




Python has this order of, it looks for an attribute inside of an object, then it looks inside the class, and then it looks inside the base classes. SInce Newclass now has __init__ defined, its not going to call the __init__ in SomeClass. If we wanted to do this, you would do:

SomeClass.__init__(self, x, y)




b = NewClass(8, 9, 10)

