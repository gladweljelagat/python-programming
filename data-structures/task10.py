#!/usr/bin/python3

# function that replaces or add key/value pairs in dictionary
def replace_key(my_dict, key, value):
    """This replaces or adds key/value pairs in a dictionary if:
    the parameter value is any type
    if the keys exists in dictionary,replace the value
    create the value if does not exist in the dictionary
    returns my_dict"""
    my_dict[key] = value
    return my_dict
