#! /usr/bin/python3
import sys
import os
from p4At import *
from Formatter import *

if len(sys.argv) < 2:
    print("filename needed as command argument")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("***file not found")
    sys.exit(1)
file = open(sys.argv[1], "r")

variable_dictionary = {}
format_dictionary = {
    "FLOW": "YES"
    , "LM": "1"
    , "RM": "80"
    , "JUST": "LEFT"
    , "BULLET": "o"}

f = Formatter(" ", format_dictionary)


# noinspection PySimplifyBooleanCheck,PyGlobalUndefined
def readCommands(file):
    """
    :param file: text file to be parsed
    :return: N/A
    """

    for input_line in file.readlines():
        input_line = input_line.rstrip('\n')  # removes newline
        if input_line == "":
            f.getformattedLine(input_line)
        token_list = input_line.split()

        if input_line != "":
            if token_list[0] == "@.":
                if token_list[1] == "VAR":
                    setvariable(input_line[6:], variable_dictionary)
                elif token_list[1] == "FORMAT":
                    if f.format_dictionary["FLOW"] == "YES":
                        printLine(f.current_working_line,f.format_dictionary,f.new_par)
                        f.clearTheLine()
                    token_list.remove("@.")
                    token_list.remove("FORMAT")
                    setformat(token_list, format_dictionary)
                elif token_list[1] == "PRINT":
                    if token_list[2] == "VARS":
                        pprint.pprint(variable_dictionary, width=30)
                    elif token_list[2] == "FORMAT":
                        pprint.pprint(format_dictionary, width=30)
            else:
                f.format_dictionary = format_dictionary
                f.variable_dictionary = variable_dictionary
                f.getformattedLine(input_line)

    if f.current_working_line != "":
        printLine(f.current_working_line, format_dictionary, f.new_par)


readCommands(file)
file.close()
