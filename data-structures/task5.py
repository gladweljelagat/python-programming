#!/usr/bin/python3

# function that deletes an item at specific position in a list

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    new_list = my_list[:idx] + my_list[idx+1:]
    return new_list


numbers = [5, 10, 15, 20, 25, 30]
print(delete_at(numbers, 3))
print(delete_at(numbers, -1))
print(delete_at(numbers, 8))
