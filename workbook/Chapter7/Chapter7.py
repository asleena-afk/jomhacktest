# Worked example 1: A reusable preview
# PRO TIP: Keyword arguments make a call easier to understand.

# def preview(text, limit=5):
#     return text.strip()[:limit]

# print(preview(" Hello world "))
# print(preview(" Hello world ", limit=8))
# print(preview(" This sucks ", limit=6))

# Worked example 2: Return several results
# PRO TIP: Keep input cleaning separate from database writes.

# def clean_fields(title, body):
#     return title.strip(), body.strip()

# title, body = clean_fields(" Hi ", " Welcome ")
# print(title)
# print(body)

# Worked example 3: Local scope
# PRO TIP Pass data into functions instead of relying on mutable globals.

# title = "Outside"
# def label():
#     title = "Inside"
#     return title

# print(label())
# print(title)

# Worked example 4: Guard clauses
# PRO TIP: A function without an explicit return returns None.
# Pro tip: if a function has no return, or reaches the end without hitting one, it gives back None.

# def can_edit(user_id, author_id):
#     if user_id is None:
#         return False
#     return user_id == author_id

# print(can_edit(None, "a"))
# print(can_edit("a", "a"))

# Exercise 1: Title validator
# YOUR TASK : Write valid_title(text) that checks the trimmed length is between 1 and 160.
# CHECK THESE CASES : Whitespace fails. 160 characters succeeds. 161 fails.
# HINT AFTER A TRY : Return a chained comparison.

def valid_title(text):
    return 1 <= len(text.strip()) <= 160

print(valid_title("   "))
print(valid_title("a" * 160))
print(valid_title("a" * 161)) # "a" * 160 is a quick way to make a 160-character string for testing.

        # How it works: 
        # text.strip() removes edge spaces first. Clean before measuring (the same lesson as Chapter 4).
        # len(...) counts the characters.
        # 1 <= ... <= 160 is a chained comparison that is true only if the length is in range. The result is already True or False, so you can return it directly.

# Exercise 2: Safe list default
# YOUR TASK : Write add_title(title, titles=None), returning a new list when none is passed.
# CHECK THESE CASES : Two calls without a list do not share items. A supplied list receives the item.
# HINT AFTER A TRY : Create [] inside the function.

def add_title(titles):
    if titles is None:
        return "New List"
    

