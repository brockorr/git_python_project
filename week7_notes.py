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
'''

# REGULAR EXPRESSIONS

'''
Using regular expressions in Python
1. Import re - this imports the regular expression library
2. dir(re) or help(re)
3. re.search method
    - ALWAYS use raw formatted strings in python
    - a_var = re.search(r"python", <var>
    - a_var.group() returns the string that was searched for, in this case "python"
    if re.search(r"python", <var>):
    - if there is a match, it will return a _sre.SRE_MATCH object, if not, it will
    -
4.In regex world Parentheses mean "Im going to save something for later
    - the period means any character, and the plus sign means one or more times.
        - so this will grab something until the end of the line, but not newline
    - a_var = re.search(r"python (.+)", <var>)
    - a_var.group() will return python and then whatever words come after python
    - a_var.group(1) will return everything after but not including python  
    - return a nonetype, so you can test against this.
    - but what if we want just the next string of characters, and not the whole line?
    - a_var = re.search(r"python (.+?) "
        - here the question mark tells it "the shortest string" and the space after )
        - tells regex which character to stop at, in this case the space character. 
    - But what if we want to add another word?
    - a_var = re.search(r"python (.+?) (.+)", a) -- I dont have a ? here becase
    - the next word is at the end of the line.
5. Regular expressions can be very cryptic, so when you encounter them in other
people code, it's very hard to understand and very time consuming to figure out 
other peoples code.

6. You can also use re.search as a conditional
    if re.search(r"platform: ", a):
        blablabla
7. re.findall
    - Put a whole file into a string and then search through it.
    - Remember, even though the whole file is in one string, the regex handles the
    - newlines fine
    - re.findall(r"python .+", cdp_data)
    - re.findall(r"python (.+)", cdp_data)
    - the difference here is the first returns a list with the word python included.
    - re.findall(r"python (.+?) (.+)", cdp_data)
        - This returns a list with a touple containing the next two words after the word python
    
'''
