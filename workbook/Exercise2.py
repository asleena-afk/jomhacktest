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
