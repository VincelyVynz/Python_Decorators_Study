# ------------------------------- Log Calls Decorator ------------------------------- #

# This decorator logs each time a function is called.
#Prints the name of the function along with the arguments passed to it and what the function returns

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"The {func.__name__} function has been called and the arguments passed in are: {args}.")
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper
