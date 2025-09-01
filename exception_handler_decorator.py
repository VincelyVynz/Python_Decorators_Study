# ------------------------------- Exception Handler ------------------------------- #

# Catches and prints any errors during function execution for easier debugging.

def error_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result                          # Returns what the original function outputs in case of no errors
        except Exception as e:                     # Catches the error instead of crashing the program.
            print(f"⚠ An Error Occurred! ⚠ {e}")   # Prints a warning message along with the error.
            return e                               # Returns the error message for easy debugging.
    return wrapper

