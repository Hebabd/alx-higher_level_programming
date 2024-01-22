#!/usr/bin/python3
def safe_print_division(a, b):
    result = 0

    try:
        result = a / b
    except ZeroDivisionError:
        reult = None
    finally:
        print('Inside resilt: {}'.format(result))
        return result
