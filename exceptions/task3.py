#!/usr/bin/python3

# integer division with debug
def safe_print_division(x, y):
    """
    This divides two integers and print result using finally.
    Assumes that the arguments are intergers.
    Returns the value of division otherwise return None.
    """
    try:
        result = x / y
    except Exception:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
