# ------------------------------- Decorators ------------------------------- #


def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"The {func.__name__} function has been called and the arguments passed in are: {args}.")
        try:
            result = func(*args, **kwargs)
            print(result)
            return result
        except ValueError:
            print("Enter a number")
        except ZeroDivisionError:
            print("⚠️ Error ⚠️")
            print("You can't divide by zero")

    return wrapper


@log_calls
def add(a, b):
    return f"The sum of {a}, {b} is {a + b}."


@log_calls
def sub(a, b):
    return f"The difference between {a} and {b} is {a - b}."


@log_calls
def mul(a, b):
    return f"The product of {a} and {b} is {a * b}."


@log_calls
def div(a, b):
    return f"The quotient of {a} when divided by {b} is {round(a / b, 2)}."

def re_run_program():
    print("\n" * 3)
    main()

def main():
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            break
        except ValueError:
            print("Please enter a number.")

    do_calc = True
    while do_calc:
        oper = input("Choose the operation you'd like to do: add, sub, mul, div. : ").lower()

        operations = {
            "add": add,
            "sub": sub,
            "mul": mul,
            "div": div
        }

        if oper in operations:
            result = operations[oper](a, b)
            if result is not None:
                do_calc = False
            do_calc = False
        else:
            print("Invalid operation. Try again.")


    rerun = input("Do you want to rerun the program? (y/n): ").lower()
    if rerun == "y":
        re_run_program()
    elif rerun == "n":
        print("Goodbye.")

main()
