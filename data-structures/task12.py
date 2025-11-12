#!/usr/bin/python3

# function that deletes keys with specific value in dictionary
def del_keys_specific_value(my_dict, specific_value_to_del):
    """This deletes keys with a specific value in a dictionary
    if the value does not exist the dictionary remain unchanged
    all keys with the searched value are deleted"""
    
    for key in keys_to_delete:
        del my_dict[key]
        return my_dict

