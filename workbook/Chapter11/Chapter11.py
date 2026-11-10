"""
Chapter 11 - HTTP, JSON and API fundamentals
Run: Windows -> py chapter_11_workbook.py   |   macOS -> python3 chapter_11_workbook.py
No packages needed.

Big picture: a CLIENT (browser, React, Swagger) sends a REQUEST to a SERVER (FastAPI).
The server sends back a RESPONSE. The API is the "contract" that says what
requests are allowed and what responses look like.

REQUEST  = method + URL + headers + (optional) body
RESPONSE = status code + headers + (optional) body
"""

import json
from urllib.parse import urlparse, parse_qs


def section(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ----------------------------------------------------------------
# EXAMPLE 1: Parts of a URL
# ----------------------------------------------------------------
section("Example 1: Parts of a URL")

# A URL is an address. Break it down:
#   http://localhost:8000/posts?limit=2
#   |      |         |    |      |
#   |      |         |    |      +-- query string (extra options, after the ?)
#   |      |         |    +--------- path (WHAT resource you want)
#   |      |         +-------------- port (WHICH program on that computer)
#   |      +------------------------ hostname (WHICH computer)
#   +------------------------------- scheme (HOW to talk: http / https)
url = urlparse("http://localhost:8000/posts?limit=2")

print(url.scheme, url.hostname, url.port)  # http localhost 8000
print(url.path)                            # /posts

# parse_qs turns the query string into a dictionary.
# Notice the value is a LIST of TEXT: {'limit': ['2']}
#   - list, because the same key can appear twice (?tag=a&tag=b)
#   - text ('2' not 2), because everything in a URL is text.
#     If you need a number, convert it: int(parse_qs(...)["limit"][0])
print(parse_qs(url.query))

# Why it matters: in FastAPI, @app.get("/posts") matches the path,
# and limit is read from the query string.
# "localhost" always means "this same computer", so the client and the
# FastAPI server are both running on YOUR machine during practice.


# ----------------------------------------------------------------
# EXAMPLE 2: Methods and intent
# ----------------------------------------------------------------
section("Example 2: Methods and intent")

# The METHOD tells the server what you want to DO with the resource.
# Same path (/posts), different method = different action.
operations = {
    "GET": "read",             # fetch data, must NOT change anything
    "POST": "create",          # make a new record
    "PUT": "replace/update",   # change an existing record
    "DELETE": "remove",        # delete a record
}

# .items() gives (key, value) pairs, so each loop gets method AND intent.
for method, intent in operations.items():
    print(method, intent)

# Real examples on the same /posts path:
#   GET    /posts        -> list posts
#   POST   /posts        -> create a post
#   PUT    /posts/p1     -> update post p1
#   DELETE /posts/p1     -> delete post p1
# Rule of thumb: GET is "safe" - calling it 10 times changes nothing.


# ----------------------------------------------------------------
# EXAMPLE 3: Status and body
# ----------------------------------------------------------------
section("Example 3: Status and body")

# The STATUS CODE is the server's short answer: did it work?
#   2xx = success      3xx = redirect
#   4xx = client error (YOU sent something wrong)
#   5xx = server error (the SERVER broke)
# 201 = Created. 204 = Success, but NO body.
status = 201
body = '{"id": "p1", "title": "Hello"}'   # body arrives as TEXT (a JSON string)

# Chained comparison: is status from 200 up to (not including) 300?
if 200 <= status < 300:
    # json.loads turns JSON text into a Python dict.
    post = json.loads(body)
    print(post["title"])   # Hello

# 201 is not 204, so this is False.
print(status == 204)       # False

# Common bug: a 204 response has an EMPTY body. json.loads("") crashes
# with an error. So: check the status first, and only parse JSON when
# there is actually a body.
# Also remember: a connection can succeed and still return 404 or 500.
# Always check the status, don't assume.


# ----------------------------------------------------------------
# EXAMPLE 4: Headers and origins
# ----------------------------------------------------------------
section("Example 4: Headers and origins")

# HEADERS are labels attached to a request/response (like info on an envelope).
# Content-Type says what format the body is in.
headers = {"Content-Type": "application/json"}

# An ORIGIN = scheme + host + port. All three must match to be "same origin".
origin = "http://localhost:5173"       # where React (the frontend) runs
api_origin = "http://localhost:8000"   # where FastAPI (the backend) runs

print(headers["Content-Type"])   # application/json
print(origin == api_origin)      # False -> different ports = different origins

# Why it matters: browsers block a page from one origin calling an API on
# another origin unless the server allows it. That rule is CORS.
# So React (5173) calling FastAPI (8000) needs CORS configured on FastAPI.
# Terminal tools (curl, Python scripts) do NOT enforce CORS - which is why
# something can work in Swagger/curl but fail in the browser.
# Security reminder: the Authorization header carries a bearer token.
# Never print real tokens.


# ----------------------------------------------------------------
# EXERCISE 1: Response classifier
# ----------------------------------------------------------------
section("Exercise 1: Response classifier")


def classify_status(status):
    """Return 'success', 'client error', 'server error' or 'other'."""
    if 200 <= status < 300:
        return "success"
    elif 400 <= status < 500:
        return "client error"
    elif 500 <= status < 600:
        return "server error"
    else:
        return "other"   # e.g. 3xx redirects


# Acceptance cases from the chapter
assert classify_status(200) == "success"
assert classify_status(204) == "success"
assert classify_status(401) == "client error"
assert classify_status(500) == "server error"
# Extra boundary checks (good habit from Chapter 9)
assert classify_status(299) == "success"
assert classify_status(300) == "other"
assert classify_status(399) == "other"
assert classify_status(400) == "client error"
assert classify_status(499) == "client error"
assert classify_status(599) == "server error"
print("Exercise 1: all checks passed")
for code in (200, 204, 401, 500):
    print(code, "->", classify_status(code))


# ----------------------------------------------------------------
# EXERCISE 2: API contract
# ----------------------------------------------------------------
section("Exercise 2: API contract")

# We are not calling a server. We are writing down WHAT the server
# should send back, using Python values.

# GET /posts -> status 200, body is a JSON LIST of post objects.
get_posts_status = 200
get_posts_body = [
    {"id": "p1", "title": "Hello"},
    {"id": "p2", "title": "Launch"},
]

# DELETE /posts/p1 -> status 204, NO body at all.
delete_status = 204
delete_body = None   # nothing to parse

# Check the contract
assert get_posts_status == 200
assert isinstance(get_posts_body, list)
assert all(isinstance(post, dict) for post in get_posts_body)
assert all("id" in post and "title" in post for post in get_posts_body)

assert delete_status == 204
assert delete_body is None   # 204 has no JSON body

# Show how a client would handle both safely:
def handle_response(status, body_text):
    """Parse JSON only when there is a body to parse."""
    if status == 204 or not body_text:
        return None
    return json.loads(body_text)

assert handle_response(200, json.dumps(get_posts_body)) == get_posts_body
assert handle_response(204, "") is None
print("Exercise 2: all checks passed")
print("GET /posts   ->", get_posts_status, json.dumps(get_posts_body))
print("DELETE       ->", delete_status, "(no body)")