# Formatter2.py
# create a text formatter, which understands:
# margins, left justification, right justification, centering, bullet lists, and variable substitution
import re
import pprint

last_format_width = -99


# noinspection PyComparisonWithNone
def expandVariables(line, dictionary):
    for key in dictionary:
        match_key = "@" + key
        line = re.sub(match_key, dictionary[key], line)


def initCurrentLine():
    line = ""
    return line


def printLine(current_line, dictionary, format_width):
    if dictionary["FLOW"] == "YES" and current_line == "":
        pass
    if dictionary["FLOW"] == "YES":
        num_of_spaces = int(dictionary["LM"]) - 2
        margin = " "
        lm_spacing = margin * num_of_spaces
        formatted_line = lm_spacing + current_line
        print(formatted_line)
    if dictionary["FLOW"] == "NO":
        num_of_spaces = int(dictionary["LM"]) - 1
        margin = " "
        lm_spacing = margin * num_of_spaces
        formatted_line = lm_spacing + current_line
        print(formatted_line)


# noinspection SpellCheckingInspection
class Formatter:

    def __init__(self, variable_dictionary, format_dictionary):
        # define instance variables
        self.variable_dictionary = variable_dictionary
        self.format_dictionary = format_dictionary
        self.current_working_line = initCurrentLine()
        self.format_width = last_format_width

    def getformattedLine(self, input_line):
        original_width = int(self.format_dictionary["RM"]) - int(self.format_dictionary["LM"]) + 1
        if self.current_working_line == "":
            Formatter.last_format_width = int(self.format_dictionary["RM"]) - int(self.format_dictionary["LM"]) + 1

        new_paragraph = False

        if input_line == "":
            if self.format_dictionary["FLOW"] == "YES":
                print(self.current_working_line)
            new_paragraph = True
            print("")

        expandVariables(input_line, self.variable_dictionary)

        if self.format_dictionary["FLOW"] == "YES":
            words = input_line.split()
            count = len(words)
            for word in words:
                length = len(word)
                if len(word) <= Formatter.last_format_width:
                    self.current_working_line = " ".join((self.current_working_line, word))
                    Formatter.last_format_width = Formatter.last_format_width - len(word) - 1
                    count = count - 1
                elif len(word) > Formatter.last_format_width:
                    printLine(self.current_working_line, self.format_dictionary, Formatter.last_format_width)
                    self.current_working_line = ""
                    self.current_working_line = " ".join((self.current_working_line, word))
                    Formatter.last_format_width = original_width
                    Formatter.last_format_width = Formatter.last_format_width - len(word) - 1
                    count = count - 1

        if self.format_dictionary["FLOW"] == "NO":
            if len(input_line) > Formatter.last_format_width:
                f_line = input_line[:Formatter.last_format_width]
                printLine(f_line, self.format_dictionary, Formatter.last_format_width)
            else:
                printLine(input_line, self.format_dictionary, Formatter.last_format_width)
        # else:
        #     printLine(self.current_working_line, self.format_dictionary, Formatter.last_format_width)