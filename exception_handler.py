# ------------------------------- Exception Handler ------------------------------- #

# Catches and prints any errors during function execution for easier debugging.

def error_catcher(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"⚠ An Error Occurred! ⚠ {e}")
            return e
    return wrapper

