#!/usr/bin/python3

# function that prints a dictionary by ordered keys
def ordered_keys(my_dict):
    """This prints a dictionary by ordered keys
    The assumptions are: all keys are strings,
    only keys are sorted at first level,
    the values can have any type."""
    for key in sorted(my_dict.keys()):
        print(f"{key}: {my_dict[key]}")
