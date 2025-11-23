#!/usr/bin/python3

def safe_print_integer(value):
    """
    This prints integer using "{:d}".formart(value).
    Returns true if the value was printed as integer,otherwise False.
    Does not import modules or use type( ).
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
