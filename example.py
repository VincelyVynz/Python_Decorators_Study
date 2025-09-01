# ------------------------------- Ice Cream example by BroCode ------------------------------- #


def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Adding sprinkles")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("Adding fudge")
        func(*args, **kwargs)
    return wrapper

@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f"Here, enjoy your {flavor} flavored ice cream")

get_ice_cream("strawberry")

print("\n" * 2)
get_ice_cream("chocolate")

