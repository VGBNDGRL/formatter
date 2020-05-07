# Formatter.py
# create a text formatter, which understands:
# margins, left justification, right justification, centering, bullet lists, and variable substitution
import re


# noinspection PyComparisonWithNone
def substituteWords(line, dictionary):
    for key in dictionary:
        matchkey = "@" + key
        line = re.sub(matchkey, dictionary[key], line)
    return line


class Formatter:

    def __init__(self, current_working_line, variable_dictionary, format_dictionary):
        # define instance variables
        self.current_line = current_working_line
        self.variable_dictionary = variable_dictionary
        self.format_dictionary = format_dictionary

    def formattedLine(self):
        line = substituteWords(self.current_line, self.variable_dictionary)
        return line
