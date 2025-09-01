import time  #importing time to measure time taken


# ------------------------------- Timer Decorator ------------------------------- #

# This decorator measures time taken by any function

def timer(func):
    def wrapper(*args, **kwargs):
        print("Starting timer")
        starting_time = time.time()
        result = func(*args, **kwargs)
        print(result)
        print("Stopping timer")
        stopping_time = time.time()
        time_elapsed = stopping_time - starting_time
        print(f"Time taken: {time_elapsed} seconds")
        return result
    return wrapper

# ------------------------------- Decorated Function (Example) ------------------------------- #

@timer
def sleeping_fn():
    sleeping_duration = int(input("Enter duration in seconds: "))
    print(f"Start sleeping for {sleeping_duration} seconds")
    time.sleep(sleeping_duration)
    return f"Slept for {sleeping_duration} seconds"


#calling the function to initiate process
sleeping_fn()