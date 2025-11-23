#!/usr/bin/python3

# function that divides a list
def list_division(my_list_1, my_list_2, list_length):
    """This divides two lists element by element.
    Returns new list of length with all divisions.
    The lists can be of any type and can be larger than either list.
    If division cannot be done return 0 and the function prints division by 0.
    If either of the list is too short the function prints out of range"""
    new_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if (not isinstance(a, (int, float))
               or not isinstance(b, (int, float))):
                print("wrong type")
                new_list.append(0)
                continue
    # Division
            result = a / b
            new_list.append(result)
        except ZeroDivisionError:
            print("division by 0")
            new_list.append(0)

        except IndexError:
            print("out of range")

        except Exception:
            new_list.append(0)


    return new_list
