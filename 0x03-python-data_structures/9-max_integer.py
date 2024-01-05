#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        retuen None
        list_copy = my_list.copy()
        list_copy.sort()
        return lit_copy[-1]
