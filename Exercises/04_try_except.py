#####
current_key = 'Mike'
default_val = 'Cohen'
dict_1 = {'John': 'Doe', 'Jane': 'Doe'}
try:
    johns = dict_1.pop(current_key)
except KeyError:  # Non-existent key
    dict_1[current_key] = default_val
    print(f"{len(dict_1)} remaining key(s) in the dictionary")
else:
    print(f"{len(dict_1)} remaining key(s) in the dictionary")
print(dict_1)

#####

tup = (1,)
try:
    a, b = tup[0], tup[1]
except IndexError as e: # takes the error massage as e
    print("IndexError")
    print(f"Exception: {e}; tup: {tup}")
    # raise # this will make the error alert
else:
    # process_data(a, b)
    print(a, b)


###### With the finally clause
def divisor(a, b):
    """
    Divides two numbers.
    a, b - numbers (int, float)
    returns a tuple of the result and a possible error.
    """
    try:
        ans = a / b
    except ZeroDivisionError as e:
        ans = None
        err = e
    except TypeError as e:
        ans = None
        err = e
    else:
        err = None
    finally:
        return ans, err


#####
try:
    # Do something that might fail
    file.write()
except PermissionError:
    # If we don't have permission to do the operation (e.g. write to protected disk), do the following
    x=5
except IsADirectoryError:
    # Trying to do a file operation on a directory - so do the following
    x=3
except (NameError, TypeError):
    # If we encouter either a non-existent variable or operation on variables, do the following
    x=2
except Exception:
    # General error, not caught by previous exceptions
    x=1
else:
    # If the operation under "try" succeeded, do the following
    x=4
finally:
    # Regardless of the result - success or failure - do this.
    x=8


##### Pythonic check and conversion
def pythonic_int_conversion(s):
    """ Convert a string to int """
    try:
        return int(s)
    except (TypeError, ValueError, OverflowError):
        return None