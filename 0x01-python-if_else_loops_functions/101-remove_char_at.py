#!/usr/bin/python3
def remove_char_at(str, n):
    length = len (str)
    if n >= 0 and n < length:
        new_str = str[:n] + str[n+1:]
        return new_str
    else:
        return str
