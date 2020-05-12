#! /usr/bin/python3
import sys
import os
import pprint
from p4At import *
from Formatter2 import *

if len(sys.argv) < 2:
    print("filename needed as command argument")
    sys.exit(1)
if not os.path.isfile(sys.argv[1]):
    print("***file not found")
    sys.exit(1)
file = open(sys.argv[1], "r")

variable_dictionary = {}
format_dictionary = {
    "FLOW": "NIL"
    , "LM": "1"
    , "RM": "80"
    , "JUST": "LEFT"
    , "BULLET": "o"}

f = Formatter(" ", format_dictionary)


# readCommands(file)

# noinspection PySimplifyBooleanCheck,PyGlobalUndefined
def readCommands(file):
    """
    :param file: text file to be parsed
    :return: N/A
    """

    for input_line in file.readlines():
        file.readline()
        # if input_line == " ":
        #     printLine(f.current_working_line, f.format_dictionary, f.new_par)
        input_line = input_line.rstrip('\n')  # removes newline
        token_list = input_line.split()

        if token_list == []:  # check for empty input
            f.new_par = False
            # print("case 4")
            # printLine(f.current_working_line, f.format_dictionary, f.new_par)
            #print("\n")
        elif token_list[0] == "@.":
            # if f.current_working_line != "":
            #     printLine(f.current_working_line, f.format_dictionary,
            #               int(f.format_dictionary["RM"]) - int(f.format_dictionary["LM"]) + 1)
            # f.current_working_line = ""
            if token_list[1] == "VAR":
                setvariable(input_line[6:], variable_dictionary)
            elif token_list[1] == "FORMAT":
                if f.format_dictionary["FLOW"] == "YES" and f.new_par == False:
                    printLine(f.current_working_line, f.format_dictionary, f.new_par)
                    print("")
                    f.clearTheLine()
                elif f.format_dictionary["FLOW"] == "YES":
                    printLine(f.current_working_line, f.format_dictionary, f.new_par)
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


readCommands(file)
if f.format_dictionary["FLOW"] == "YES":
    if f.current_working_line != "":
        print("case 5")
        printLine(f.current_working_line,f.format_dictionary, f.new_par)
        print("\n")
file.close()
