# CHAPTER 08
# Modules, packages, objects and type annotations
# Modules = from library to import 
# # & packages = 

# Worked example 1: Import a standard module
# PRO TIP: Path handles Windows and macOS separators.
# WHY IT BEHAVES THIS WAY: Path is an imported class. The / operator joins path components.

# from pathlib import Path
# path = Path("posts") / "draft.json"
# print(path.name)
# print(path.suffix)

# Worked example 2: A class and an instance
# PRO TIP: A method call such as client.auth.get_user() follows the same object pattern.
# WHY IT BEHAVES THIS WAY: # __init__ initializes the instance. self refers to the instance receiving the method call.

# class Post:
#     def __init__(self,title: str):
#         self.title = title.strip()
#     def preview(self) -> str:
#         return self.title[:5]

# post = Post("  Hello world  ")
# print(post.preview())


# Worked example 3: Annotations and optional values
# PRO TIP: Pydantic later uses annotations to validate incoming data.
# WHY IT BEHAVES THIS WAY: The union annotation permits a string or None. The function still contains the behavior.

# def image_label(path: str | None) -> str:
#     return "No image" if path is None else path

# print(image_label(None))
# print(image_label("a/photo.png"))

# Worked example 4: Qualified names and entry points
# PRO TIP : Project modules use imports such as from postlight.config import settings.
# WHY IT BEHAVES THIS WAY : The entry-point guard runs main() only when this file is executed directly.

import json
def main():
    print(json.dumps({"ok": True}))

if __name__ == "__main__":
    main()




