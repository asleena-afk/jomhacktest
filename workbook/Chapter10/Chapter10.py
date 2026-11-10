# CHAPTER 10
# Files, JSON, virtual environments and configuration

# Worked example 1: JSON round trip
# PRO TIP : UUID and datetime need conversion before JSON serialization
# WHY IT BEHAVES THIS WAY : JSON null maps to Python None. JSON booleans use lowercase true and false

import json
post = {"title": "Hello", "image": None}
encoded = json.dumps(post)
decoded = json.loads(encoded)
print(encoded)
print(decoded == post)
# print(decoded)


# Worked example 2: A temporary text file
# PRO TIP : Use UTF-8 explicitly for portable text files.
# WHY IT BEHAVES THIS WAY : The file closes before reading. The temporary directory is removed when the block ends.

# from pathlib import Path
# from tempfile import TemporaryDirectory
# with TemporaryDirectory() as folder:
#     path = Path(folder) / "draft.txt"
#     with path.open("w", encoding="utf-8") as file:
#         file.write("Hello, JomCode")
#     print(path.read_text(encoding="utf-8"))


# Worked example 3: Configuration defaults
# PRO TIP : Use pydantic-settings in the application to load .env.
# WHY IT BEHAVES THIS WAY : getenv() reads the process environment. It does not automatically load a .env file.

# import os
# origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
# print(origin)
# print(bool(os.getenv("SUPABASE_DB_URL")))


# Worked example 4: Check the active interpreter
# PRO TIP : Windows can use .venv\Scripts\python.exe directly without activating PowerShell scripts.
# WHY IT BEHAVES THIS WAY : python -m pip installs into the interpreter you invoke. A different terminal can select a different zenvironment

# import sys
# from importlib.metadata import PackageNotFoundError, version
# print(sys.executable)
# try:
#     print(version("fastapi"))
# except PackageNotFoundError:
#     print("FastAPI is not installed in this interpreter")

# Exercise 1: Store a draft
# YOUR TASK : Write a post dictionary to JSON in a temporary directory, read it and verify the title.
# CHECK THESE CASES : Unicode title survives. Missing image remains None.
# HINT AFTER A TRY : Use json.dumps(..., ensure_ascii=False) and UTF-8.








# Exercise 2: Required setting
# YOUR TASK : Write a function that reports a missing setting without printing its value.
# CHECK THESE CASES : Missing or empty value raises ValueError. A present value returns successfully.
# HINT AFTER A TRY : Read with os.getenv and test truthiness.



