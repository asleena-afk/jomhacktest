# Worked example 1: Title length rules
# PRO TIP: Clean before measuring
# # Why “clean before measuring” matters: if you measured before stripping, " Hello " would be 7 characters. And a title of just spaces (" ") would look like 3 valid characters, but after strip() it’s 0, which correctly fails.

# title = "  Hello  ".strip()
# valid = 1 <= len(title) <= 160
# if valid:
#     print("Ready")
# else:
#     print("Check Title")

# Worked example 2: Choose one status
# PRO TIP: Put specific cases before broader cases
# # Why “specific before broader”: imagine you wrote views < 100 first. Then 0 views would also match it and show “Growing” instead of “New”. The order matters because only the first match runs.
# # Common mistake: if views = 0 (one =) is an error, because = assigns a value. == compares.

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
# # The pro tip, in plain words: hiding the Edit button only changes what the user sees. Someone technical could still send an edit request directly. So the server must run this same ownership check before saving anything. Think of it as the button being a sign on the door, and the server check being the actual lock.

# signed_in = True
# user_id = "user_a"
# author_id = "user_b"
# can_edit = signed_in and user_id == author_id
# print(can_edit)
# print(not signed_in)

# Worked example 4: Missing and empty values
# PRO TIP: Use is None for the missing-value check
# https://claude.ai/share/55966a71-7433-4e24-bafa-66a4c6475a2f

# image_path = None
# if image_path is None:
#     print("No image")          # Lines 1-3: What is means: is asks, “Is this the very same thing?” None exists only once in all of Python, so is None is the cleanest way to ask “is this missing?”
# title = ""
# if not title:
#     print("Blank title")
# print(image_path == title)

# if image is None:      # was an image provided at all?
# if not title:          # is the title empty?


# Exercise 1: Publishing decision
# YOUR TASK : Allow publishing only when signed in and a trimmed title has 1 to 160 characters.
# CHECK THESE CASES : Signed out fails. Whitespace title fails. " Hello " succeeds when signed in.
# HINT AFTER A TRY: Combine the two checks with and.
    
# signed_in = True
# title = " Hello ".strip()
# title_ok = 1 <= len(title) <= 160
# can_publish = signed_in and title_ok

# if can_publish:    
#     print("Published")
# else:
#     print("Cannot Publish")

# CLAUDE
# signed_in = True
# title = " Hello "

# clean_title = title.strip()
# title_ok = 1 <= len(clean_title) <= 160
# can_publish = signed_in and title_ok

# if can_publish:
#     print("Published")
# else:
#     print("Cannot publish")

# Exercise 2: Image size decision
# YOUR TASK : Classify an upload as missing, acceptable or too large. Limit it to 5 MiB.
# CHECK THESE CASES : None is missing. Exactly 5 MiB is acceptable. One byte more is too large.
# HINT AFTER A TRY : Check None before comparing numbers.

# size_bytes = 5_242_880
# size_Mib = size_bytes / 1_048_576

# if size_Mib == 0:
#     label = "Missing"
# elif size_Mib <= 5:
#     label = "Acceptable"
# else:
#     label = "Too Large"
# print(label)

# CLAUDE
# max_bytes = 5 * 1_048_576
# size_bytes = None

# if size_bytes is None:
#     label = "Missing"
# elif size_bytes <= max_bytes:
#     label = "Acceptable"
# else:
#     label = "Too large"

# print(label)