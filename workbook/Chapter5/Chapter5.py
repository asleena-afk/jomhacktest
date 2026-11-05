# CHAPTER 05
# List [], Tuple (), Dictionary {k: v}, Set {}

# Worked example 1: A list of titles
# PRO TIP: Accessing an index outside the list raises IndexError.
# WHY IT BEHAVES THIS WAY : Lists preserve insertion order. Index zero is the first item and -1 is the last.
# Append only works on list, doesn't work on multiple data list
    # Line by line
    # titles = ["Hello", "Learning"] creates a list with 2 items.
    # titles.append("Launch") adds a new item to the end. The list is now ["Hello", "Learning", "Launch"].
    # titles[0] gives the first item. Python counts from 0, not 1, so it prints Hello.
    # titles[-1] gives the last item. Negative numbers count from the end, so it prints Launch.
    # len(titles) counts the items, so it prints 3.

# titles = ["Hello", "Learning"]
# titles.append("Launch")
# print(titles[0])
# print(titles[-1])
# print(len(titles))
# print(titles[2])

# ****Watch out: titles[3] would crash with IndexError, because the last valid index is 2.****

# Worked example 2: A post dictionary
# PRO TIP: post["missing"] raises KeyError. 
# WHY IT BEHAVES THIS WAY : Keys identify fields. get() returns None for a missing key unless a default is supplied.
# Key is the dictionary, value is the data 
# {dictionary1, dictionary2} --> {"key1": "value1", "key2": "value2"}
# print(key[variables])
    # Line by line
    # The dictionary has two key-value pairs: key "id" holds "p1" and key "title" holds "Hello".
    # post["title"] = "Updated" replaces the value stored under "title".
    # print(post["title"]) prints Updated.
    # post.get("image_path") looks for a key that doesn’t exist. get() returns None instead of crashing.
    # "title" in post checks whether the key exists, so it prints True.
        # [] vs .get()
        # post["image_path"] raises KeyError because the key is missing.
        # post.get("image_path") returns None.
        # post.get("image_path", "no image") returns "no image". The second argument is your own default.

        # ****Use [] when the key must exist. Use .get() when it might not.****

# post = {
#     "id": "p1",
#     "title": "Hello"
#     }
# post["title"] = "Updated"
# print(post["title"])
# print(post.get("image_path"))

# Worked example 3: Tuples and unique authors
# PRO TIP: Do not rely on set iteration order.
# WHY IT BEHAVES THIS WAY: Tuple unpacking assigns both dimensions. A set removes duplicates; sorted() makes display order predictable
    # Line by line
    # Tuple part
    # (640, 480) is a tuple, a fixed pair of values that can’t be changed after creation.
    # width, height = dimensions is called unpacking. The first value goes to width and the second to height.
    # It prints 640 480.

    # Set part
    # {"Ada", "Lin", "Ada"} has “Ada” twice, but a set keeps only one copy, so it becomes {"Ada", "Lin"}.
    # Sets have no reliable order, so printing a set directly could show the items in any order.
    # sorted(authors) returns a list in alphabetical order: ['Ada', 'Lin'].

# dimensions = (640, 480)
# width, height = dimensions
# authors = {"Ada", "Lin", "Ada"}
# print(width,height)
# print(sorted(authors))
# print(dimensions)

# Worked example 4: Copies and shared references
# PRO TIP: A shallow copy still shares nested mutable values.
# WHY IT BEHAVES THIS WAY : alias refers to the same dictionary. copy() creates a separate outer dictionary.
    #Line by line
    # This is the trickiest one. Think of a variable as a name tag, not a box.

    # post = {...} creates one dictionary and sticks the name tag post on it.
    # alias = post does not create a new dictionary. It sticks a second name tag on the same one.
    # copy = post.copy() makes a brand new, separate dictionary with the same contents.
    # alias["title"] = "Changed" changes the dictionary that post and alias both point to.

    # Result
    # print(post["title"]) prints Changed, because post and alias are the same dictionary.
    # print(copy["title"]) prints Original, because copy is separate and was not affected.
    # post  ──┐
    #         ├──► {"title": "Changed"}
    # alias ──┘
    # copy  ─────► {"title": "Original"}

        # Pro tip explained: .copy() is a shallow copy. 
        # If the dictionary contains another list or dictionary inside it, that inner object is still shared between the original and the copy. 
        # You’ll only run into this with nested data.

# post = {"title": "Original"}
# alias = post
# copy = post.copy()
# alias["title"] = "Changed"
# print(post["title"])
# print(copy["title"])
# print(alias)
# print(post)

# Exercise 1: Post collection
# YOUR TASK : Create two post dictionaries in a list and update only the second title.
# CHECK THESE CASES : List length stays two. The first title stays Hello. Second becomes Revised.
# HINT AFTER A TRY : Index the list, then access the dictionary key.

# posts = [
#     {"id": "p1", "title": "Hello"},
#     {"id": "p2", "title": "Learning"},
# ]

# posts[1]["title"] = "Revised"

# print(len(posts))
# print(posts[0]["title"])
# print(posts[1]["title"])

    # Here is a hint: posts[1] gets the second dictionary, then ["title"] gets the field inside it.
    # Why it works: posts[1] picks the second dictionary in the list, and ["title"] = "Revised" changes only that dictionary’s title field. The first dictionary is never touched, and no items were added or removed, so the length stays 2.

# Exercise 2: Unique formats
# YOUR TASK : Count unique supported formats from a list containing duplicates.
# CHECK THESE CASES : PNG, JPEG, PNG, WEBP has three unique formats. Original list remains unchanged.
# HINT AFTER A TRY : Convert to a set and use len().

formats = ["PNG", "JPEG", "PNG", "WEBP"]
unique = set(formats)

print(len(unique))
print(formats)
print(len(formats))

    # Hint: a set automatically removes duplicates, and len() counts items.
    # Why it works: set(formats) builds a new set from the list, so formats is untouched and still shows all 4 items, duplicates included. The set holds only PNG, JPEG and WEBP, so len() gives 3.

