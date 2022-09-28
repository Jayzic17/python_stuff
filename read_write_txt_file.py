import sys, fileinput, os, re

# Note: all of this code works, but it isn't meant to be run; just to look at.
# This is purely hear just to remember how to read and write to a file in Python.

# Read from .txt file
txt_file = open(sys.argv[2], 'r')
file_content = txt_file.read()
tag_list = file_content.split('\n')
txt_file.close()

firstLine = True
hasBadTags = False
hasIncorrectTags = False
foundName = False
currentName = ""
currentKey = ""
currentInstance = ""

missingTags = ["list of tags", "here"]
key_criteria = "(^regex's)|(here)"
value_criteria = {
    "dictionary": "^of",
    "regexe's": "^here"
}

# Write to a .txt file
with open(sys.argv[1], 'a') as file: # mode 'a' appends lines to the end of the file. Mode 'w' overrites whatever's in there already
    file.write(sys.argv[2][:-13] + '\n')
    for line in tag_list:
        if re.search("^blah", line) != None:
            if not firstLine:
                    if not hasIncorrectTags and missingTags != []:
                        file.write(currentName[9:] + '\n')
                        file.write(' '.join(missingTags))
                    elif not hasIncorrectTags and missingTags == []:
                        file.write("")
                    else:
                        file.write("blah")
                    missingTags = ["list", "here"]
                hasIncorrectTags = False
                firstLine = False
                currentInstance = line
            elif foundName:
                currentName = line
                foundName = False
            elif re.search("blah", line) != None:
                foundName = True
            else:
                currentKey = ""           