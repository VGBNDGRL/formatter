#! /usr/bin/python3
import re
import numbers

# regular expressions
keyvarRE = re.compile(r'[^@].*?(?==)')
formatRE = re.compile(r'\w+(?=\s*=[^/])')
valRE = re.compile(r'[^=]*$')


def setvariable(inputline, dictionary):
    """
    :param inputline: tokens to be validated
    :param dictionary: token will be added to this dictionary
    :return: N/A
    """
    tokenstring = inputline.strip(' ')

    if tokenstring[0] == "@":
        result = validvar(tokenstring)
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

    key = keyvarRE.search(tokenstring).group()

    if key != None:
        value = valRE.search(tokenstring).group()
        if value != None:
            value = value.strip('\"')
            valid = True
        else:
            print('***Invalid, should follow format "key=value')
    else:
        print('***Invalid, should follow format "key=value')
    return key, value, valid


def setformat(tokenlist, dictionary):
    """
    :param tokenlist: token to be validated
    :param dictionary: token will be added to this dictionary
    :return: N/A
    """

    # go thru each tag and check its validity (LM, RM, JUST, BULLET, FLOW)
    for token in tokenlist:
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
    key = formatRE.search(token).group()
    value = valRE.search(token).group()
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
