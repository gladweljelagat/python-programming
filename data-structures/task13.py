#!/usr/python3

# function that returns key value with the biggest interger value
def high_score(student_name):
    """This returns key value with biggest integer value.
    Assumes all values are integers.
    Assumes all students have different scores.
    If no score found return None."""
    if not student_name:
        return None
    return max(student_name, key=student_name.get)
