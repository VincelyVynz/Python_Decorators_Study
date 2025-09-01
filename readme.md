# 🧩 Python Decorators Study

This repository contains small but practical examples of Python decorators. Each file explores a specific use case with clear comments for easier understanding of how decorators work and how they can be useful in real-world programs.

---

## 📁 File Overview

| File Name                              | Description                                                                                                                       |
|---------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| `main.py`                             | Shows a simple template for creating and using decorators. Demonstrates basic decorator syntax.                                   |
| `log_calls_decorator.py`              | Defines the `log_calls` decorator. Logs the function name, arguments, and return value every time a decorated function is called. |
| `log_calls_with_calculator_example.py`| Uses the `log_calls` decorator in a small calculator-style program. Demonstrates decorators with user input and error handling.   |
| `timer_decorator.py`                  | Defines the `timer` decorator to calculate and print the time taken by a function.                                                |
| `timer_decorator_with_example.py`     | Contains the `timer` decorator along with an example using `time.sleep()` to simulate a delay.                                    |
| `exception_handler_decorator.py`      | Defines the `error_catcher` decorator, which wraps a function with try-except and prints any errors that occur.                   |
| `exception_handler_with_example.py`   | Demonstrates the `error_catcher` decorator by wrapping a function that performs division and may raise a `ZeroDivisionError`.     |
| `testfile.py`                         | A sandbox file used for quick testing and trying out code during development. *(Not essential to the main examples.)*             |

---

## 🔧 Decorators Included

### `@log_calls` — Log Function Calls
- **File:** `log_calls_decorator.py`
- **Purpose:** Logs when a function is called, including its name, arguments, and result.
- **Used in:** `log_calls_with_calculator_example.py`

---

### `@timer` — Measure Execution Time
- **File:** `timer_decorator.py`
- **Purpose:** Measures and prints how long a function takes to run.
- **Example:** See `timer_decorator_with_example.py`

---

### `@error_catcher` — Handle Exceptions 
- **File:** `exception_handler_decorator.py`
- **Purpose:** Wraps a function with a try-except block and prints the error type, error message and traceback if one occurs for easier debugging.
- **Example:** See `exception_handler_with_example.py`

---

## 🚀 How to Run

You can import any decorator module into your own Python scripts and apply the decorators to your functions.
Or, run the example files directly to see how each decorator works in practice.