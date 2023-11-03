#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = argv[1]
    b = argv[3]
    op = argv[2]
    if op == '+':
        print("{} {} {} = {}".format(a, op, b, add(int(a), int(b))))
    elif op == '-':
        print("{} {} {} = {}".format(a, op, b, sub(int(a), int(b))))
    elif op == '*':
        print("{} {} {} = {}".format(a, op, b, mul(int(a), int(b))))
    elif op == '/':
        print("{} {} {} = {}".format(a, op, b, div(int(a), int(b))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
