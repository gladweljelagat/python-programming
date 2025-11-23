#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    """
    This prints upto x elements of my_list on the same line,
    followed by a new line.
    Returns the real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except Exception:
            break
        if i != x - 1:
            print(" ", end="")
    print()
    return count
