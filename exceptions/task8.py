#!/usr/bin/python3

# function that excecutes a function safely
def safe_function(fct, *args, **kwargs):
    """This assumes that the parameter fct is always a pointer to a function.
    Returns the result of the function upon success.
    Otherwise prints an exception error to stderr and returns None."""
    try:
        return fct(*args, **kwargs)
    except Exception as e:
        # print the exception to stderr
        import sys
        print("Exception:", e, file=sys.stderr)
        return None
