#!/usr/bin/python3

from task8 import safe_function


def division(a, b):
    return a / b


# calling the function
result = safe_function(division, 10, 2)
print(result)


# calling the function
result = divisionfe_function(divide, 10, 0)
print(result)
