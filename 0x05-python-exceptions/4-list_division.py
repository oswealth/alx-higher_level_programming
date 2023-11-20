#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except (TypeError, ZeroDivisionError, IndexError) as e:
            if isinstance(e, TypeError):
                print("wrong type")
            elif isinstance(e, ZeroDivisionError):
                print("division by 0")
            elif isinstance(e, IndexError):
                print("out of range")
            result = 0
        finally:
            new_list.append(result)
    return new_list
