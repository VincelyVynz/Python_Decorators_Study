from timer_decorator import timer
from exception_handler_decorator import error_catcher


@error_catcher
@timer
def div(a, b):
    return a / b

div(10,0)