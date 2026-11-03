print("hello we are learning python")

name = "Ada"
age = 25
height = 1.65
is_member = False
nickname = None

print(f"Type of name: {type(name).__name__}")
print(f"Type of age: {type(age).__name__}")
print(f"Type of height: {type(height).__name__}")
print(f"Type of is_member: {type(is_member).__name__}")
print(f"Type of nickname: {type(nickname).__name__}")

print(type(name).__name__)
print(type(age).__name__)
print(type(height).__name__)
print(type(is_member).__name__)
print(type(nickname).__name__)

print(type(name))
print(type(age))
print(type(height))
print(type(is_member))
print(type(nickname))

first = 4_200_000
second = 750_000
total = first + second
print(total)
print(f"Total size: {total} bytes")
total_mb = total / 1_000_000
print(f"Total size: {total_mb} MB")
total_mib = total / 1_048_576
print(f"Total size in MiB: {total_mib:.2f} MiB")

size1 = 4_200_000
size2 = 750_000
size3 = 1_048_576

mb1 = size1 / 1_000_000
mb2 = size2 / 1_000_000
mib3 = size3 / 1_048_576

print(f"{mb1} MB")
print(f"{mb2} MB")
print(f"{mib3} MiB")

name = " JomCoder_99 "
clean_name = name.strip().lower()
print(f"NAME: '{clean_name}'")
characters = len(clean_name)
print(f"No of Characters: {characters}")
print(clean_name[:6])

raw = "  JomCoder_99  "
username = raw.strip().lower()

print(username)
print(len(username))
print(username[:6])

for raw in ["  JomCoder_99  ", "  GO  ", " CraXXY778"]:
    username = raw.strip().lower()
    print(username)
    print(len(username))
    print(username[:6])
    print("-----")

text1 = "15"
text2 = "27"
total = int(text1) + int(text2) 

print(text1 + text2)
print(total)
print(f"{total} comments")
print(f"{int(text1) + int(text2)} comments")