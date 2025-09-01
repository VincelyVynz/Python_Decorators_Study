# ------------------------------- Exception Handler ------------------------------- #
import traceback


# Catches and prints any errors during function execution for easier debugging.

def error_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result                          # Returns what the original function outputs in case of no errors
        except Exception as e:                     # Catches the error instead of crashing the program.
            print(f"⚠ An Error Occurred! ⚠")       # Prints a warning message along with the error.
            print(f"Error Type: {type(e).__name__}")
            print(f"Error Message: {e}")
            print(f"Traceback: {traceback.format_exc()}")
            return e                               # Returns the error message for easy debugging.
    return wrapper


# Example (Trying to divide by zero.

@error_catcher
def divide(a, b):
    return a / b

divide(10, 0)  # Will trigger ZeroDivisionError, but won't crash.
