import time

def timer(func):
    def wrapper(*args, **kwargs):
        print("Starting timer")
        result = func(*args, **kwargs)
        print("Stopping timer")
        print(result)
        return result
    return wrapper


@timer
def sleeping_fn():
    sleeping_duration = int(input("Enter duration in seconds: "))
    print(f"Start sleeping for {sleeping_duration} seconds")
    time.sleep(sleeping_duration)
    return f"Slept for {sleeping_duration} seconds"


sleeping_fn()