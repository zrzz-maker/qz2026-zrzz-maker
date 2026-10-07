def divide(a, b):
    try:
        x = float(a)
        y = float(b)
        r = x / y
        return r
    except ValueError:
        return None
    except ZeroDivisionError:
        return None