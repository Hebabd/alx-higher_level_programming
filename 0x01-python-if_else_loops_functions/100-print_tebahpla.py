#!/usr/bin/python3
    i = 122
    while i >= 97:
        flag = 0
        if i % 2 != 0:
            i = i - 32
            flag = 1
            print("{:s}".format(chr(i)), end="")
            if flg == 1:
                i = i + 32
                i = i - 1
