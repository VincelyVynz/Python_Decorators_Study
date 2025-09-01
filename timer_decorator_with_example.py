import time  #importing time to measure time taken


# ------------------------------- Timer Decorator ------------------------------- #

# This decorator measures time taken by any function

def timer(func):
    def wrapper(*args, **kwargs):
        print("Starting timer")
        starting_time = time.time()                       # Stores the starting time
        result = func(*args, **kwargs)                    # The decorated function is executed
        print(result)
        stopping_time = time.time()                       # Stores stopping time
        time_elapsed = stopping_time - starting_time      # Calculates time taken
        print(f"Stopping timer\nTime taken: {time_elapsed:.4f} seconds")  # Prints time taken
        return result                                 # Returns what's returned by the function
    return wrapper

# ------------------------------- Decorated Function (Example) ------------------------------- #

#Example decorated function

@timer
def sleeping_fn():
    sleeping_duration = int(input("Enter duration in seconds: "))
    print(f"Start sleeping for {sleeping_duration} seconds")
    time.sleep(sleeping_duration)
    return f"Slept for {sleeping_duration} seconds"


#calling the function to initiate process
sleeping_fn()