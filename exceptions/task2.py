#!/usr/bin/python3

# function that print and count integers
def safe_print_list_integers(my_list=[], x=0):
    """
    Prints the first x elements of a list that are integers on the same line
    followed by a new line.
    The parameter my_list can contain any type.
    x represent the number of elements to print
    x can be bigger than length of my_list
    Returns the real number of integers printed)
    """
    count = 0
    printed = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printed += 1
        except (ValueError, TypeError):
            # not an integer skip it
            continue
        except IndexError:
            # Out of range stop the loop
            break
    print()
    return printed
