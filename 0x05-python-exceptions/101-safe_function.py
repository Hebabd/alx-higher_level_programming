#!/usr/bin/python3
    import sys

    def safe_function(fc, *args):
        try:
            resolve = fct(*args)
        except Exception as ex:
            print(ex, file=sys.stderr)
            return None
        else:
            return resolve
