# ------------------------------- Decorators ------------------------------- #

# Decorator function template:

def decorator_func(original_func):
    def wrapper(*args, **kwargs):
        print(f"Calling {original_func.__name__}")
        return original_func(*args, **kwargs)
    return wrapper


#To add a decorator before a function, the decorator function name is entered before the function on which the decorator is to be added, with an `@` symbol.

@decorator_func
def original_func(a, b):
    pass

# Multiple decorators can be stacked but might affect the behaviour based on the order of stacking