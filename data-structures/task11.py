#!/usr/bin/python3

# function that deletes a key in a dictionary
def delete_key(my_dict, key):
    """This  function deletes a key in the dictionary if it exists.
    The key is always the string.
    If the key does not exist return the original dictionary unchanged"""
    if key in my_dict:
        del my_dict[key]
        return my_dict
