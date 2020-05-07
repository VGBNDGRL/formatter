# Formatter.py
# create a text formatter, which understands:
# margins, left justification, right justification, centering, bullet lists, and variable substitution
import re


# noinspection PyComparisonWithNone
def substituteWords(line, dictionary):
    token_list = line.split()

    for token in token_list:
        new_token = re.sub('[.!@,]', '', token)
        if dictionary.get(new_token) != None:
            value = dictionary.get(new_token)
            new_token = "@" + new_token
            line = re.sub(new_token, value, line)
    return line


class Formatter:

    def __init__(self, current_working_line, variable_dictionary, format_dictionary):
        # define instance variables
        self.current_line = current_working_line
        self.variable_dictionary = variable_dictionary
        self.format_dictionary = format_dictionary

    def formattedLine(self):
        line = substituteWords(self.current_line, self.variable_dictionary)
        print(line)
