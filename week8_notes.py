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


Part 2

THe unique thing aboout python modules is they create their own namespace. 
Namespaces are like dns domain names. 
[module].[var]

Python modules have their own namespace.BaseException

The __name__  is called a special name variable. It's how you can separate
imported code from main code. If you call the __name__variable in a main file, it will return __main__
if you call it in a referenced file, it will print the module name.BaseException

You can separate executable code from module code in the following way.

if __name__ == '__main__':
    bla
    bla
    bla


PACKAGES

>>>import pprint sys
>>>pprint.pprint(sys.path)
this returns a list of places that python uses to try to find modules and packages.
A modlue is a python file. A python package is a directory in your filesystem that is constructed in a special way.

To make the directory a package, all you have to do (prior to py33) is create a file __init__.py in the directory.

WHat you can do in the package directory is import modules (files) from packages (directory)
    import package.module
    or from packagage import module


What hapens when you load a package is __init__.py is executed.
This makes it so you can have integrated sets of code that you can integrate with one command. 

'''
import week8_module

week8_module.some_func_1()
week8_module.some_func_2()
week8_module.some_func_3()
