"""
HW01 — Library Barcodes → Book Titles (Chaining)

Implement a tiny hash table with chaining.
Do not add type hints. Use only the standard library.
"""

def make_table(m):
    """Return a new table with m empty buckets (lists)."""
    # Step 4: build the data structure (list of lists)
    return [[] for _ in range(m)]

def hash_basic(s):
    """Return a simple integer hash for string s.
    Hint: sum ordinals of characters.
    """
    # Step 5–6: compute a stable integer from s
    return sum(ord(c) for c in s)

def put(t, key, value):
    """Insert or overwrite (key, value) in table t using chaining."""
    if key is None:
        return  # ignore invalid keys

    m = len(t)
    h = hash_basic(key)
    index = h % m
    bucket = t[index]

    # Check if key exists; overwrite if found
    for i, (k, v) in enumerate(bucket):
        if k == key:
            bucket[i] = (key, value)
            return
    # Otherwise append new pair
    bucket.append((key, value))

def get(t, key):
    """Return value for key or None if not present."""
    m = len(t)
    h = hash_basic(key)
    index = h % m
    bucket = t[index]

    for k, v in bucket:
        if k == key:
            return v
    return None

def has_key(t, key):
    """Return True if key exists in table t; else False."""
    m = len(t)
    h = hash_basic(key)
    index = h % m
    bucket = t[index]

    for k, _ in bucket:
        if k == key:
            return True
    return False

def size(t):
    """Return total number of stored pairs across all buckets."""
    return sum(len(bucket) for bucket in t)

if __name__ == "__main__":
    # Optional manual check
    t = make_table(5)
    put(t, "B123", "Data Structures")
    put(t, "L001", "Linear Algebra")
    put(t, "C777", "Algorithms")
    print(t)
    print("Size:", size(t))
    print("Get B123:", get(t, "B123"))
    print("Has L001:", has_key(t, "L001"))
