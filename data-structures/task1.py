#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]


my_list = [2, 5, 7, 9, 11]
print(element_at(my_list, 0))
print(element_at(my_list, 2))
print(element_at(my_list, 5))
print(element_at(my_list, -1))
