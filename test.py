from timer_decorator import timer
from exception_handler_decorator import error_catcher
from log_calls_decorator import log_calls


@timer
@error_catcher
def div(a, b):
    return a / b

div(10,0)