#! /usr/bin/python3
import re
import numbers

# regular expressions
key_regex = re.compile(r'[^@].*?(?==)')
format_regex = re.compile(r'\w+(?=\s*=[^/])')
value_regex = re.compile(r'[^=]*$')


def setvariable(input_line, dictionary):
    """
    :param input_line: tokens to be validated
    :param dictionary: token will be added to this dictionary
    :return: N/A
    """
    token_string = input_line.strip(' ')

    if token_string[0] == "@":
        result = validvar(token_string)
        # if valid add to dictionary
        if bool(result[2]):
            dictionary[result[0]] = result[1]
    else:
        print('***Not a recognizable command, should be "@key=value"')


# noinspection PyComparisonWithNone
def validvar(tokenstring):
    """
    :param tokenstring: tokens to be validated
    :return key: can hold string or None
    :return value: can hold string or None
    :return valid: True if 'key:val' format is followed, otherwise False
    """
    valid = False
    value = None
    key = None

    key = key_regex.search(tokenstring).group()

    if key != None:
        value = value_regex.search(tokenstring).group()
        if value != None:
            value = value.strip('\"')
            valid = True
        else:
            print('***Invalid, should follow format "key=value')
    else:
        print('***Invalid, should follow format "key=value')
    return key, value, valid


def setformat(token_list, dictionary):
    """
    :param token_list: token to be validated
    :param dictionary: token will be added to this dictionary
    :return: N/A
    """

    # go thru each tag and check its validity (LM, RM, JUST, BULLET, FLOW)
    for token in token_list:
        result = validformat(token)
        if bool(result[2]):
            # if valid add to dictionary
            dictionary[result[0]] = result[1]


def validformat(token):
    """

    :param token: validated to check if it follows 'tag:val' format
    :return key: can hold string or None
    :return value: can hold string or None
    :return valid: True if 'key:val' format is followed, otherwise False
    """
    key = format_regex.search(token).group()
    value = value_regex.search(token).group()
    valid = False

    if key == "LM" or key == "RM":
        if int(value):
            valid = True
        else:
            print("***Invalid value, found:" + value)
    elif key == "JUST":
        if value == "LEFT" or value == "RIGHT" or value == "BULLET" or value == "CENTER":
            valid = True
        else:
            print("***Invalid value, found:" + value)
    elif key == "FLOW":
        if value == "YES" or "NO":
            valid = True
        else:
            print("***Invalid value, found:" + value)
    elif key == "BULLET":
        if value == "o":
            valid = True
        else:
            print("***Invalid value, found:" + value)
    else:
        print("***Invalid key, found:" + key)
    return key, value, valid
