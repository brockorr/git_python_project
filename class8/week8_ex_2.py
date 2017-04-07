#!/usr/bin/python
import show_version

'''
the with as statment is a clean way of adding the contents of the file into the variable
'''

def main():
    with open("show_version.txt", "r") as version_file:
        show_ver = version_file.read()
    
    #print "Model: "+(show_version.obtain_model(show_ver))
   # print "%15s: %-50s" % ("model", model)
    print "%15s: %-70s" % ("Model", (show_version.obtain_model(show_ver)))
    print "%15s: %-50s" % ("Version", (show_version.obtain_os_version(show_ver)))
    print "%15s: %-50s" % ("Uptime", (show_version.obtain_uptime(show_ver)))

if __name__ == "__main__":
    main()