# CHAPTER 06
# Loops and data processing learn

# Worked example 1: Number each post
# PRO TIP: Prefer iteration over indexing when you need the value.
# for loop title = [List]

# titles = ["Hello", "Launch", "Sharp", "Mainframe"]
# for number, title in enumerate(titles, start=1):
#     print(f"{number}. {title}")

# Worked example 2: Filter and transform
# PRO TIP: Use an ordinary loop if a comprehension becomes hard to read.

# posts = [{"title": "Hello", "views": 2},
#          {"title": "Launch", "views": 12},
#          {"title": "", "views": 15}]
# popular = [p["title"].upper() for p in posts
#            if p["views"] >= 10]
# print(popular)

# Worked example 3: A bounded while loop
# PRO TIP: Real API retries also need delay and retryable-error checks.

# attempt = 0
# while attempt < 3:
#     attempt += 1
#     print(f"Attempt {attempt}")

# Worked example 4: Totals and early exit
# PRO TIP: sum(views) is a concise alternative for a numeric total.
# break = exit logic

# views = [3, 0, 7, 6, 8, 10]
# total = 0
# for value in views:
#     total += value
# print(total)
# for value in views:
#     if value == 0:
#         print("Unviewed post found")
#         break

# Exercise 1: Search titles
# YOUR TASK : Return titles containing the search text, ignoring case.
# CHECK THESE CASES : "py" matches Python Tips. Empty search matches every title.
# HINT AFTER A TRY: Normalize both strings with lower().

titles = ["hello", "radio", "cars", "Python Tips"]
print(titles)




# Exercise 2: Author counts
# YOUR TASK : Count posts per author using a dictionary.
# CHECK THESE CASES : Ada, Lin, Ada gives Ada=2 and Lin=1. Empty input produces {}.
# HINT AFTER A TRY : Use counts.get(author, 0) + 1.


authors = ["Ada", "Lin", "Ada"]
# posts = 