#!/usr/bin/python3

# function that prints an integer with error message
def safe_print_integer_error(value):
    """Prints integer with type checking in "{:d}".format())format.
    Parameter value can be of any type.
    Returns true if the value printed was an integer.
    Otherwise, prints an exception error to stderr and returns false."""
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError) as e:
        # Print the exception to stderr
        import sys
        print("Exception:", e, file=sys.stderr)
        return False
