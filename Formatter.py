# Formatter2.py
# create a text formatter, which understands:
# margins, left justification, right justification, centering, bullet lists, and variable substitution
import re


# noinspection PyComparisonWithNone
def expandVariables(line, dictionary):
    for key in dictionary:
        match_key = "@" + key
        line = re.sub(match_key, dictionary[key], line)
    # return line


# def empty_string(current_working_line, beginning):
#     current_working_line = ""
#     beginning = True


def formatLine(input_line, current_working_line, dictionary):
    format_width = int(dictionary["RM"]) - int(dictionary["LM"]) + 1
    new_paragraph = False

    if input_line == "":
        if dictionary["FLOW"] == "YES":
            print(current_working_line)
        new_paragraph = True
        print("")

    expandVariables(input_line, dictionary)

    if dictionary["FLOW"] == "YES":
        words = input_line.split()
        for word in words:
            length = len(word)
            if len(word) < format_width:
                current_working_line = " ".join((current_working_line, word))
                # current_working_line = current_working_line + word
                format_width = format_width - len(word)
            else:
                print(current_working_line)

    if dictionary["FLOW"] == "NO":
        if len(input_line) > format_width:
            f_line = input_line[:format_width]
            printLine(f_line, dictionary, format_width)
        else:
            printLine(input_line, dictionary, format_width)


def printLine(current_working_line, dictionary, format_width):
    if dictionary["FLOW"] == "YES" and current_working_line == "":
        pass

    num_of_spaces = int(dictionary["LM"]) - 1
    margin = " "
    lm_spacing = margin * num_of_spaces
    formatted_line = lm_spacing + current_working_line
    print(formatted_line)


class Formatter:

    def __init__(self, input_line, variable_dictionary, format_dictionary):
        # define instance variables
        self.input_line = input_line
        self.variable_dictionary = variable_dictionary
        self.format_dictionary = format_dictionary
        self.beginning = False
        self.current_working_line = input_line

    def formatAndPrint(self):
        formatLine(self.input_line, self.current_working_line, self.format_dictionary)
