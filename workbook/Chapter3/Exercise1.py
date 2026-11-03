title = "  How to Code  "
published = True
image_path = None
first = "12"
second = "8"
total = int(first) + int(second)
preview = title.strip()

print(f"Title: {preview}")
print(f"Preview: {preview[:5]}")
print(f"Total views: {total}")
print(f"Published: {published}")
print(f"Image path: {image_path}")
print(f"Total posts published: {total}")
print(f"Total posts published: {total}, Image path: {image_path}, Published: {published}, Total views: {total}, Preview: {preview[:5]}, Title: {preview}")
print("Go"[:5])

title = "My  Story".upper()
raw_email = "Jom101@example.com"
email = raw_email.strip().lower()
report_size = 2_000_000
report_size_mb = report_size / 1_000_000

print(f"Title: {title}")
print(f"Raw Email: {raw_email}")
print(f"Email: {email}")
print(f"Report Size: {report_size_mb} MB")
print(f"Report Size: {report_size_mb:.5f} MB")
