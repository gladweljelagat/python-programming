#!/usr/bin/python3


# function that returns a set of all elements present only in one set
def return_all_elements(x, y):
    """This returns all the elements of only one set in two sets"""
    result = x.symmetric_difference(y)
    return result
