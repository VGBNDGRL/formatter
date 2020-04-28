#! /usr/bin/python3
import sys
import os
import pprint
from p4At import setformat, setvariable

if len(sys.argv) < 2:
    print("filename needed as command argument")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("***file not found")
    sys.exit(1)
file = open(sys.argv[1], "r")

variableDict = {}
formatDict = {
    "FLOW": "YES"
    , "LM": "1"
    , "RM": "80"
    , "JUST": "LEFT"
    , "BULLET": "o"}

def readCommands(file):
    """
    :param file: text file to be parsed
    :return: N/A
    """

    while True:
        inputLine = file.readline()  # reads a text line at a time from file
        if inputLine == "": # check for empty input
            break
        inputLine = inputLine.rstrip('\n')  # removes newline
        tokenlist = inputLine.split()

        # go thru tokens if we have valid func calls
        if tokenlist[0] == "@.":
            if tokenlist[1] == "VAR":
                setvariable(inputLine[6:], variableDict)
            elif tokenlist[1] == "FORMAT":
                tokenlist.remove("@.")
                tokenlist.remove("FORMAT")
                setformat(tokenlist, formatDict)
            elif tokenlist[1] == "PRINT":
                if tokenlist[2] == "VARS":
                    pprint.pprint(variableDict, width=30)
                elif tokenlist[2] == "FORMAT":
                    pprint.pprint(formatDict, width=30)
            else:
                print("*** Not a recognizable command, found:" + inputLine)
        else:
            print("*** Not a recognizable command, found:" + inputLine)

readCommands(file)
file.close()
