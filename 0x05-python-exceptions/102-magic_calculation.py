#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            except Exception:
                result = b + a
                break
            finally:
                result += (a ** b) / i
    return result
