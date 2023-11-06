#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if length == 0:
        total = (0, None)
        return total
    else:
        tally = (length, sentence[0:1])
        return tally
