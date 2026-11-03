# Worked example 1: Title length rules
# PRO TIP: Clean before measuring

# title = "  Hello  ".strip()
# valid = 1 <= len(title) <= 160
# if valid:
#     print("Ready")
# else:
#     print("Check Title")

# Worked example 2: Choose one status
#PRO TIP: Put specific cases before broader cases

# views = 25
# if views == 0:
#     label = "New"
# elif views < 100:
#     label = "Growing"
# else:
#     label = "Popular"
# print(label)

# Worked example 3: Ownership decision
# PRO TIP:A hidden edit button is only a UI rule; the server must also check ownership.

# signed_in = True
# user_id = "user_a"
# author_id = "user_b"
# can_edit = signed_in and user_id == author_id
# print(can_edit)
# print(not signed_in)

# Worked example 4: Missing and empty values
# PRO TIP: Use is None for the missing-value check

# image_path = None
# if image_path is None:
#     print("No image")
# title = ""
# if not title:
#     print("Blank title")
# print(image_path == title)

image_path = None
if image_path is None:
    print("No image")
title = "mmmm"
if not title:
    print("Blank title")
print(image_path == title)