# CHAPTER 09
# Errors, debugging and basic testing

# Worked example 1: Handle a known conversion error
# PRO TIP : Avoid a bare except that hides unrelated bugs.
# WHY IT BEHAVES THIS WAY : Only ValueError is handled. Unexpected failures remain visible.

# def parse_count(text):
#     try:
#         return int(text)
#     # except ValueError:
#     #     return None
#     except ValueError as e:
#         return e

# print(parse_count("12"))
# print(parse_count("twelve"))

# Worked example 2: Raise a useful error
# PRO TIP : Use an exception message that identifies the violated rule.
# WHY IT BEHAVES THIS WAY : Raising an exception prevents invalid data from continuing through the program.

def clean_title(text):
    title = text.strip()
    if not title:
        raise ValueError("Title is required")
    return title

try:
    print(clean_title("  "))
except ValueError as error:
    print(error)

# Worked example 3: Boundary assertions
# PRO TIP : Assertions can be disabled; use explicit validation for user input
# WHY IT BEHAVES THIS WAY : Boundary checks catch off-by-one mistakes at the upload limit.

# def allowed_size(size):
#     return 0 < size <= 5 * 1024 * 1024

# assert not allowed_size(0)
# assert allowed_size(5 * 1024 * 1024)
# assert not allowed_size(5 * 1024 * 1024 + 1)
# print("3 checks passed")

# Worked example 4: Inspect intermediate values
# PRO TIP : Set a breakpoint before the assertion and inspect both variables
# WHY IT BEHAVES THIS WAY : repr() reveals whitespace that ordinary output can hide. A debugger can inspect these values without extra prints.

# raw = "    Hello    "
# cleaned = raw.strip()
# print(repr(raw), len(raw))
# print(repr(cleaned), len(cleaned))
# assert len(cleaned) == 5
# assert len(raw) == 13
# print("All passed")

# Exercise 1: Nonnegative counts
# YOUR TASK : Convert numeric text to a nonnegative integer or return None.
# CHECK THESE CASES : "0" gives 0. "-1" and "abc" give None.
# HINT AFTER A TRY : Catch ValueError, then check the numeric range.






# Exercise 2: Regression checks
# YOUR TASK: Test title cleaning for a normal, blank and overlong title.
# CHECK THESE CASES : Normal title succeeds. Blank and 161-character titles raise ValueError.
# HINT AFTER A TRY : Use a loop and explicitly fail if an invalid case succeeds




