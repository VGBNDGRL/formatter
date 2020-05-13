# Formatter.py
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
    return line


def printLine(current_line, dictionary, new_par):
    if dictionary["FLOW"] == "YES":
        if dictionary["JUST"] == "BULLET":
            if current_line == "":
                return
            if new_par:
                num_of_spaces = " " * (int(dictionary["LM"]) - 1)
                formatted_line = dictionary["BULLET"] + current_line
                print(num_of_spaces + formatted_line)
                new_par = False
            else:
                num_of_spaces = " " * (int(dictionary["LM"]))
                formatted_line = current_line
                print(num_of_spaces + formatted_line)
        else:
            if current_line == "":
                return
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
        self.current_working_line = ""
        self.format_width = last_format_width
        self.new_par = False

    def clearTheLine(self):
        self.current_working_line = ""
        self.new_par = True

    def getformattedLine(self, input_line):
        original_width = int(self.format_dictionary["RM"]) - int(self.format_dictionary["LM"]) + 1
        if self.current_working_line == "" and self.format_dictionary["JUST"] != "BULLET":
            Formatter.last_format_width = int(self.format_dictionary["RM"]) - int(self.format_dictionary["LM"]) + 1
        if self.current_working_line == "" and self.format_dictionary["JUST"] == "BULLET":
            Formatter.last_format_width = int(self.format_dictionary["RM"]) - int(self.format_dictionary["LM"])

        if input_line == "":
            if self.format_dictionary["FLOW"] == "YES":
                printLine(self.current_working_line, self.format_dictionary, self.new_par)
            self.clearTheLine()
            print("")
            return

        else:
            input_line = expandVariables(input_line, self.variable_dictionary)
            if self.format_dictionary["FLOW"] == "YES":
                words = input_line.split()
                count = len(words)
                for word in words:
                    length = len(word)
                    if self.format_dictionary["JUST"] == "BULLET":
                        if len(word) < Formatter.last_format_width:
                            self.current_working_line = " ".join((self.current_working_line, word))
                            Formatter.last_format_width = Formatter.last_format_width - len(word) - 1
                        else:
                            printLine(self.current_working_line, self.format_dictionary, self.new_par)
                            if self.format_dictionary["JUST"] == "BULLET":
                                self.clearTheLine()
                                self.new_par = False
                            else:
                                self.clearTheLine()
                            self.current_working_line = " ".join((self.current_working_line, word))
                            Formatter.last_format_width = original_width
                            Formatter.last_format_width = Formatter.last_format_width - len(word) - 2
                    else:
                        if len(word) <= Formatter.last_format_width:
                            self.current_working_line = " ".join((self.current_working_line, word))
                            Formatter.last_format_width = Formatter.last_format_width - len(word) - 1
                        else:
                            printLine(self.current_working_line, self.format_dictionary, self.new_par)
                            if self.format_dictionary["JUST"] == "BULLET":
                                self.clearTheLine()
                                self.new_par = False
                            else:
                                self.clearTheLine()
                                self.current_working_line = " ".join((self.current_working_line, word))
                                Formatter.last_format_width = original_width
                                Formatter.last_format_width = Formatter.last_format_width - len(word) - 1

            elif self.format_dictionary["FLOW"] == "NO":
                if len(input_line) > Formatter.last_format_width:
                    f_line = input_line[:Formatter.last_format_width]
                    printLine(f_line, self.format_dictionary, self.new_par)
                else:
                    printLine(input_line, self.format_dictionary, self.new_par)
                    return
