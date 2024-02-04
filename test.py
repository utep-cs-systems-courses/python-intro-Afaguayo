#! /usr/bin/env python3

from sys import argv
import os, stat
from collections import defaultdict
import re

# commands to read and choose what file to write to in our case we do "python3 test.py declaration.txt output.txt"
declarationFileName = argv[1] #read this file
declarationOutputName = argv[2] #write to this file

# Check if file to read exist.
if not os.path.exists(declarationFileName):
    os.write(2, ("File %s does not exist\n" % declarationFileName).encode())

# Check is file to write to exist.
if not os.path.exists(declarationOutputName):
    os.write(2, ("Word count output file %s does not exist\n" % declarationOutputName).encode())

# get os to get file to open
fdOutput = os.open(declarationOutputName, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, stat.S_IRWXU)
# get os to get file to read
fdReader = os.open(declarationFileName, os.O_RDONLY)


# (Get file to read, get the files total byte size) and store file contents.
declarationStorage = os.read(fdReader, os.path.getsize(declarationFileName))

# Separate the file text with space, period, comma, colon, semi-comma, and --,-,'
separator = (r'\s|,\s|\.|\;|\:|\--|\-|\'').encode()
# Store the words again
declarationStorage = re.split(separator, declarationStorage)
#  Create dictionary
outputDictionary = defaultdict(int)

# Run as long as there is contents in the file and add to key. If already exist increment.
for key in declarationStorage:
    outputDictionary[key.lower().decode()] += 1

# Sort the words in ascending order in a tuple.
outputDictionary = sorted(outputDictionary.items())
# Slice the first element.
outputDictionary = outputDictionary[1::]

#  Get the tuple of (word, value) and combine it to one string and write to output file.
for word,value in outputDictionary:
    words = (word + " " + str(value) + "\n").encode()
    os.write(fdOutput, words)