# Homework – Functions

Solve at least **one** question (recommended to try more)

Submit your solutions as **Python code**

## Question 1 – Print numbers in range (no return)

Write a function that gets **two int parameters**: `start` and `stop`

The function should **print** all numbers from `start` to `stop` (inclusive)

Notes:

* This function **does not return** a value
* Use a loop (`for` with `range`) inside the function

### Demo (example usage)

```python
print_numbers(3, 7)
# expected output:
# 3
# 4
# 5
# 6
# 7
```

## Question 2 – Basic math list (returns a list)

Write a function that gets **two numbers** `a` and `b` and returns a list in this exact order:

`[a+b, a-b, a/b, a*b]`

Notes:

* The function **returns** the list
* Assume `b != 0` (no need to handle division by zero)

### Demo (example usage)

```python
result = basic_math_list(10, 2)
print(result)
# expected output:
# [12, 8, 5.0, 20]
```

## ✨✨ Question 3 – Bonus challenge: Mini math game -- Experts only! ✨✨

Implement a small game

The computer should:

* Pick a random number between **1 and 10**
* Pick a random operation from: `+`, `-`, `*`, `%`
* Pick another random number between **1 and 10**
* Print the equation and ask the user for the result

Rules:

* If the user is correct, print `Correct!`
* Otherwise print `Wrong.. the answer was ___`

### Your task

You will get the **main code** below

Your job is to complete the missing functions:

* `get_random_between_1_10()`
* `get_random_operation()`
* `calc_result(num1, oper, num2)`

### Main code (DO NOT CHANGE)

```python
num1 = get_random_between_1_10()
oper = get_random_operation()
num2 = get_random_between_1_10()
result = calc_result(num1, oper, num2)

print(f"{num1} {oper} {num2} = ?")
user_result = int(input('whats the result? '))

if result == user_result:
    print('Correct!')
else:
    print(f"Wrong.. the answer was {result}")
```

### Starter code (complete the TODOs)

```python
import random


def get_random_between_1_10() -> int:
    """Return a random integer between 1 and 10 (inclusive)."""
    # TODO: implement
    pass


def get_random_operation() -> str:
    """Return a random operation symbol: one of '+', '-', '*', '%'"""
    # TODO: implement
    pass


def calc_result(num1: int, oper: str, num2: int) -> int:
    """Calculate and return the result of: num1 oper num2

    Supported operations: +, -, *, %

    Example:
        calc_result(7, '*', 3) -> 21
    """
    # TODO: implement
    pass
```

### Demo (example run)

Example 1:

```text
8 * 4 = ?
whats the result? 32
Correct!
```

Example 2:

```text
9 % 2 = ?
whats the result? 3
Wrong.. the answer was 1
```

Submit email: *[pythonai211225+python14func1@gmail.com](mailto:pythonai211225+python14func1@gmail.com)*
