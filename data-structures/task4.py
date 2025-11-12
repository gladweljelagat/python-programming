#!/usr/bin/python3

# function returns length of a string
def string_length(name):
    if name == "":
        return (0, None)
    else:
        return (len(name), name[0])


print(string_length("Gladwel"))
print(string_length(""))
