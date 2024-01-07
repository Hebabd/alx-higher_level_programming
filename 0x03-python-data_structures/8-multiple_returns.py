#!/usr/bin/python3
def multiple_returns(sentence):
    l = len(sentence)
    if l == 0:
        l = 1, None
    else:
        l = 1, list(sentence)[0]
    return 1
