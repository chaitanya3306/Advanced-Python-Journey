# ------------------------------------------------------
# 📘 Day 5: Context Managers (with, __enter__/__exit__, contextlib)
# ------------------------------------------------------
# Read + run these examples. They are production-style and commented.
# ------------------------------------------------------

"""
WHY CONTEXT MANAGERS?
- Ensure setup/cleanup around a code block.
- Cleanup runs even if errors happen.
- Use `with ... as ...:` to acquire a resource and release it safely.
"""

# --- Built-in example: files ---
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello from Day 5!\n")
# <-- file closed automatically

# --- Build your own with __enter__/__exit__ ---
class ManagedResource:
    def __init__(self, name: str):
        self.name = name
        self.open = False

    def __enter__(self):
        self.open = True
        print(f"[enter] Opened {self.name}")
        return self

    def __exit__(self, exc_type, exc, tb):
        self.open = False
        print(f"[exit] Closed {self.name}")
        # Return True to suppress exception, False/None to propagate:
        return False

with ManagedResource("resource-1") as r:
    print("Using:", r.name)

# --- Suppressing errors example ---
class SwallowErrors:
    def __enter__(self):
        print("Enter SwallowErrors")
        return self

    def __exit__(self, exc_type, exc, tb):
        if exc_type:
            print(f"Suppressed: {exc_type.__name__} -> {exc}")
            return True  # suppress
        return False

with SwallowErrors():
    1 / 0  # suppressed
print("Still alive!")

# --- Function-style with contextlib.contextmanager ---
from contextlib import contextmanager

@contextmanager
def temporary_file(path: str, mode: str = "w", encoding: str = "utf-8"):
    f = open(path, mode, encoding=encoding)
    try:
        yield f
    finally:
        f.close()

with temporary_file("temp.txt") as f:
    f.write("temporary data\n")

# --- Handy helpers: suppress, closing, ExitStack ---
from contextlib import suppress, closing, ExitStack
import urllib.request

with suppress(KeyError):
    {}["missing"]  # ignored

# closing: for objects that need close() but lack __enter__/__exit__
# (Commented to avoid network in some environments)
# with closing(urllib.request.urlopen("https://example.com")) as resp:
#     _ = resp.read(50)

# ExitStack: dynamic number of contexts
paths = ["a.txt", "b.txt", "c.txt"]
with ExitStack() as stack:
    files = [stack.enter_context(open(p, "w", encoding="utf-8")) for p in paths]
    for i, f in enumerate(files, 1):
        f.write(f"file #{i}\n")

# --- Real-world utilities ---

# Timer context: measure block duration
import time
from typing import Optional

class Timer:
    def __init__(self, label: str = "timer"):
        self.label = label
        self.start: Optional[float] = None
        self.elapsed: Optional[float] = None

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc, tb):
        self.elapsed = time.perf_counter() - (self.start or 0.0)
        print(f"[{self.label}] took {self.elapsed:.4f}s")
        return False

with Timer("compute"):
    sum(range(1_000_00))

# Temporary chdir: auto-revert
import os

@contextmanager
def chdir(path: str):
    old = os.getcwd()
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    try:
        yield
    finally:
        os.chdir(old)

print("cwd before:", os.getcwd())
with chdir("playground"):
    print("cwd inside:", os.getcwd())
print("cwd after:", os.getcwd())

# Thread lock usage (pattern)
import threading
lock = threading.Lock()
def critical_section():
    with lock:
        # thread-safe operations
        pass

# --- Most Important to Remember ---
"""
1) Context managers guarantee cleanup (use `with`).
2) Class-based: implement __enter__ (setup) and __exit__ (cleanup).
3) __exit__ return True to suppress errors; False/None to re-raise.
4) Function-based: use @contextmanager with try/finally.
5) Tools: contextlib.suppress, closing, ExitStack for dynamic/nested resources.
6) Common use cases: files, locks, DB connections, timing, temp dirs/settings.
"""
# ------------------------------------------------------
