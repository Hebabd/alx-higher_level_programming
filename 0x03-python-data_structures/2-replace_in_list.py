#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
   listlength = len(my_list) - 1
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
