#!/usr/bin/python

'''
MODULES

Modules are basically files in python that contain code for something.
they can contain functions or classes and methods? 
They are usually imported into another file

A python module is just a python file
we need them because we want to be able to re-use code
this could be either your own code or code from others.

They promote code-reusability

Import method vs from import method - difference pertains to namespace.

WHen yyou do import {file} it brings the module name in your local name space
which means that you access the module components by typing in the file name
This can be confirmed by  doing dir(), which will show you the module name is imported
into the local namespace. To be clear, when it imports the module, it will 
execute the whole file, which means if you have something in the main section
of the file, then it will execute that stuff.

from {file} import {something} - THis is bringing the something into your local
namespace and you do not have to prepend it with your local namespace.This
method also executes the whole file

you can also import something AS, which means you can rename the namespace
of a module. 

from file import something as zz


'''
import week8_module
