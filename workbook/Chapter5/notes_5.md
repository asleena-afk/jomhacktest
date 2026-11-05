# Chapter 5 explained: lists, tuples, dictionaries and sets

Think of the four collection types like this:

| Type | Real-life picture | Ordered? | Can change? | Duplicates? |
|---|---|---|---|---|
| List `[]` | A queue of posts | Yes | Yes | Allowed |
| Tuple `()` | A fixed pair like (width, height) | Yes | No | Allowed |
| Dictionary `{k: v}` | A form with labelled fields | Yes (by insertion) | Yes | Keys must be unique |
| Set `{}` | A guest list where each name appears once | No | Yes | Removed automatically |

## Other types

### More built-in types

| Type | What it is | Example |
|---|---|---|
| `frozenset` | A set that can't change | `frozenset({"PNG", "JPEG"})` |
| `range` | A sequence of numbers | `range(1, 4)` gives 1, 2, 3 |
| `str` | Text, also a sequence of characters | `"Hello"[0]` gives `"H"` |
| `bytes` / `bytearray` | Raw binary data (files, images) | `b"abc"` |

### Standard library collections (need an import, no install)

| Type | What it's for |
|---|---|
| `Counter` | Counting items. Replaces the `counts.get(author, 0) + 1` pattern |
| `defaultdict` | A dictionary with automatic default values |
| `deque` | A list that is fast to add or remove from both ends |
| `namedtuple` / `dataclass` | A record with named fields, like a tidier post dictionary |

**Note:** Stick to list, tuple, dictionary and set for now. `Counter` and `dataclass` are the ones to look at later.