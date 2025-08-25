# ---------------------------
# 📘 Advanced Python Notes – Day 2
# Topic: Function Arguments (*args, **kwargs, etc.)
# ---------------------------

"""
👉 Most Important Points to Remember:
1. *args → Collects extra positional arguments as a tuple.
2. **kwargs → Collects extra keyword arguments as a dictionary.
3. You can mix normal args, default args, *args, and **kwargs in the same function.
4. Order matters: 
   def func(normal, default=10, *args, kw_only, **kwargs)
5. Argument unpacking:
   - func(*list_or_tuple) → expands into positional arguments
   - func(**dict) → expands into keyword arguments
6. Keyword-only arguments:
   - Defined after * or *args in the function signature.
"""

# ---------------------------
# Examples
# ---------------------------

# 1. Basic *args
def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))   # 10


# 2. Basic **kwargs
def greet(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

greet(name="Chaitanya", lang="Python")


# 3. Mixing args and kwargs
def intro(name, *hobbies, **details):
    print("Name:", name)
    print("Hobbies:", hobbies)
    print("Details:", details)

intro("Chaitanya", "Coding", "Cricket", age=21, country="India")


# 4. Argument unpacking
nums = [1, 2, 3]
print(add_all(*nums))  # same as add_all(1, 2, 3)

info = {"name": "Chaitanya", "lang": "Python"}
greet(**info)


# 5. Keyword-only arguments
def book_flight(source, destination, *, seat="Economy"):
    print(f"Flying {source} → {destination} in {seat} class.")

book_flight("Mumbai", "London", seat="Business")

