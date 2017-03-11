#!/usr/bin/python

'''

CLASS 7

FILES and REGULAR EXPRESSIONS

FILES
<varname> = open("path/to/file/file.txt") -- for windows this needs to be a rawstring because windows uses the escape character \



'''
# Open A file
f = open("PyNotes_Throwaway.txt")
# read A single line
f.readline()
# Now read the lines out
# Readline and readlines make each line an entry in a list.
f.readlines()
# If you did readlines again, it will return an empty list because readlines is already at the end of the file.
# To go back to the top of the list:
f.seek(0)
# f.read will return the whole file as a string instead of a list.
f.read()
# You can also iterate over the file. Let's start at the top again and strip off the new line seq
f.seek(0)
for line in f:
	print line.strip("\n")

# WRITING DATA
'''
BASIC PROCEDURE:

1. If you want to write to the file without appending:
f = open("newfile", "w")
f.write("test\n")
f.close()

2. If you're creating a new file
f = open("newfile", "w")
f.write("test\n")
a = "another string"
f.write(a)
# Note, often the OS has not actually written the changes to the file until you flush it or close it.
f.flush()
f.close()

3. If you're appending a new file, the file pointer (the cursor) automatically is at the end of the file because of the a.
f = open("newfile", "a")
f.write("test\n")
a = "another string"
f.write(a)
# Note, often the OS has not actually written the changes to the file until you flush it or close it.
f.flush()
f.close()

GOTCHAS:


1. Windodws stores newlines as carriage return newlines, backslash r, backslash n. Python converts these things automatically.
	- if youre RWing binary data on windows, the conversion that python automaticallly does can ruin the data.
	- To fix this for reading files
		f = open("read_file", "rb")
	- and for writing files
		f = open("read_file", "wb")

2. Its best practice  to close yor file gracefully, but the open and close statements can occasionally not work the best.

THE MORE PROPER way to open and close:
with open("newfile", r or w) as <varname>:
	f.readline()
	f.readline()
# with will automatically close the file after the indent.

the advantage of using the with method is it automatically ensures you will do a close on the file, even if you forget
