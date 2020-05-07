# Formatter.py
# create a text formatter, which understands:
# margins, left justification, right justification, centering, bullet lists, and variable substitution


class Formatter:

    def __init__(self, current_working_line, variable_dictionary, format_dictionary):
        # define instance variables
        self.current_line = current_working_line
        self.variable_dictionary = variable_dictionary
        self.format_dictionary = format_dictionary

    # define class methods
    @classmethod
    def substituteWords(cls, input_line):
        print("This is subtituteWords")