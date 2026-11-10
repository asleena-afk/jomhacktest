# Press Ctrl + Shift + V (or Cmd + Shift + V on Mac) to see the formatted version.

Built-in Data Types
In programming, data type is an important concept.

Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:
| Category | Types |
|---|---|
| Text | `str` |
| Numeric | `int`, `float`, `complex` |
| Sequence | `list`, `tuple`, `range` |
| Mapping | `dict` |
| Set | `set`, `frozenset` |
| Boolean | `bool` |
| Binary | `bytes`, `bytearray`, `memoryview` |
| None | `NoneType` |

## Escape characters

Other escape characters used in Python. Source: https://www.w3schools.com/python/python_strings_escape.asp

| Code | Result |
|---|---|
| `\'` | Single quote |
| `\\` | Backslash |
| `\n` | New line |
| `\r` | Carriage return |
| `\t` | Tab |
| `\b` | Backspace |
| `\f` | Form feed |
| `\ooo` | Octal value |
| `\xhh` | Hex value |

## Python keywords

Reserved words that cannot be used as variable names, function names or any other identifiers. Source: https://www.w3schools.com/python/python_ref_keywords.asp

| Keyword | Description |
|---|---|
| `and` | A logical operator |
| `as` | To create an alias |
| `assert` | For debugging |
| `async` | Define an asynchronous function |
| `await` | Wait for and get a result from an awaitable |
| `break` | To break out of a loop |
| `case` | Pattern in a match statement |
| `class` | To define a class |
| `continue` | To continue to the next iteration of a loop |
| `def` | To define a function |
| `del` | To delete an object |
| `elif` | Used in conditional statements, same as else if |
| `else` | Used in conditional statements |
| `except` | Used with exceptions, what to do when an exception occurs |
| `False` | Boolean value, result of comparison operations |
| `finally` | Used with exceptions, a block of code that runs whether or not there is an exception |
| `for` | To create a for loop |
| `from` | To import specific parts of a module |
| `global` | To declare a global variable |
| `if` | To make a conditional statement |
| `import` | To import a module |
| `in` | To check if a value is present in a list, tuple, etc. |
| `is` | To test if two variables are the same object |
| `lambda` | To create an anonymous function |
| `match` | Start a match statement (compare a value against cases) |
| `None` | Represents a null value |
| `nonlocal` | To declare a non-local variable |
| `not` | A logical operator |
| `or` | A logical operator |
| `pass` | A null statement, does nothing |
| `raise` | To raise an exception |
| `return` | To exit a function and return a value |
| `True` | Boolean value, result of comparison operations |
| `try` | To make a try...except statement |
| `while` | To create a while loop |
| `with` | Used to simplify exception handling |
| `yield` | To return values one at a time from a generator |

## Python random module

A built-in module for making random numbers. Source: https://www.w3schools.com/python/module_random.asp

| Method | Description |
|---|---|
| `seed()` | Initialize the random number generator |
| `getstate()` | Returns the current internal state of the random number generator |
| `setstate()` | Restores the internal state of the random number generator |
| `getrandbits()` | Returns a number representing the random bits |
| `randrange()` | Returns a random number between the given range |
| `randint()` | Returns a random number between the given range |
| `choice()` | Returns a random element from the given sequence |
| `choices()` | Returns a list with a random selection from the given sequence |
| `shuffle()` | Takes a sequence and puts it in a random order |
| `sample()` | Returns a given sample of a sequence |
| `random()` | Returns a random float between 0 and 1 |
| `uniform()` | Returns a random float between two given parameters |
| `triangular()` | Returns a random float between two parameters, with an optional mode as the midpoint |
| `betavariate()` | Random float between 0 and 1 based on the Beta distribution (statistics) |
| `expovariate()` | Random float based on the Exponential distribution (statistics) |
| `gammavariate()` | Random float based on the Gamma distribution (statistics) |
| `gauss()` | Random float based on the Gaussian distribution (probability) |
| `lognormvariate()` | Random float based on a log-normal distribution (probability) |
| `normalvariate()` | Random float based on the normal distribution (probability) |
| `vonmisesvariate()` | Random float based on the von Mises distribution (directional statistics) |
| `paretovariate()` | Random float based on the Pareto distribution (probability) |
| `weibullvariate()` | Random float based on the Weibull distribution (statistics) |

## Python string methods

All string methods return a new value. They do not change the original string. Source: https://www.w3schools.com/python/python_strings_methods.asp

| Method | Description |
|---|---|
| `capitalize()` | Converts the first character to upper case |
| `casefold()` | Converts the string to lower case (stronger than `lower()`, for comparing text) |
| `center()` | Returns a centered string |
| `count()` | Returns how many times a value appears in the string |
| `encode()` | Returns an encoded version of the string |
| `endswith()` | Returns True if the string ends with the given value |
| `expandtabs()` | Sets the tab size of the string |
| `find()` | Returns the position of a value, or -1 if not found |
| `format()` | Formats specified values in a string |
| `format_map()` | Formats values in a string using a dictionary |
| `index()` | Returns the position of a value, or raises an error if not found |
| `isalnum()` | True if all characters are letters or numbers |
| `isalpha()` | True if all characters are letters |
| `isascii()` | True if all characters are ASCII characters |
| `isdecimal()` | True if all characters are decimals |
| `isdigit()` | True if all characters are digits |
| `isidentifier()` | True if the string is a valid identifier |
| `islower()` | True if all characters are lower case |
| `isnumeric()` | True if all characters are numeric |
| `isprintable()` | True if all characters are printable |
| `isspace()` | True if all characters are whitespace |
| `istitle()` | True if the string follows title rules |
| `isupper()` | True if all characters are upper case |
| `join()` | Joins the items of an iterable into one string |
| `ljust()` | Returns a left-justified version of the string |
| `lower()` | Converts the string to lower case |
| `lstrip()` | Removes whitespace from the left side |
| `maketrans()` | Returns a translation table for `translate()` |
| `partition()` | Splits the string into a tuple of three parts |
| `replace()` | Replaces a value with another value |
| `rfind()` | Returns the last position of a value, or -1 if not found |
| `rindex()` | Returns the last position of a value, or raises an error |
| `rjust()` | Returns a right-justified version of the string |
| `rpartition()` | Like `partition()`, but splits at the last match |
| `rsplit()` | Splits the string into a list, starting from the right |
| `rstrip()` | Removes whitespace from the right side |
| `split()` | Splits the string into a list at a separator |
| `splitlines()` | Splits the string at line breaks into a list |
| `startswith()` | Returns True if the string starts with the given value |
| `strip()` | Removes whitespace from both ends |
| `swapcase()` | Swaps lower case to upper case and vice versa |
| `title()` | Converts the first character of each word to upper case |
| `translate()` | Returns a translated string |
| `upper()` | Converts the string to upper case |
| `zfill()` | Pads the start of the string with zeros |

## Arithmetic operators

Used with numbers to do maths. Source: https://www.w3schools.com/python/python_operators_arithmetic.asp

| Operator | Name | Example |
|---|---|---|
| `+` | Addition | `x + y` |
| `-` | Subtraction | `x - y` |
| `*` | Multiplication | `x * y` |
| `/` | Division | `x / y` |
| `%` | Modulus | `x % y` |
| `**` | Exponentiation | `x ** y` |
| `//` | Floor division | `x // y` |

Example with `x = 15` and `y = 4`:

| Expression | Result |
|---|---|
| `x + y` | 19 |
| `x - y` | 11 |
| `x * y` | 60 |
| `x / y` | 3.75 |
| `x % y` | 3 |
| `x ** y` | 50625 |
| `x // y` | 3 |

Two kinds of division:

- `/` always returns a float, for example `12 / 5` gives 2.4.
- `//` rounds down to the nearest whole number, for example `12 // 5` gives 2.

## Comparison operators

Used to compare two values. They return `True` or `False`. Source: https://www.w3schools.com/python/python_operators_comparison.asp

| Operator | Name | Example |
|---|---|---|
| `==` | Equal | `x == y` |
| `!=` | Not equal | `x != y` |
| `>` | Greater than | `x > y` |
| `<` | Less than | `x < y` |
| `>=` | Greater than or equal to | `x >= y` |
| `<=` | Less than or equal to | `x <= y` |

Chaining comparisons: `1 < x < 10` does the same as `1 < x and x < 10`.