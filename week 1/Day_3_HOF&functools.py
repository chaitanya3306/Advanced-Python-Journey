# 📘 Day 3: Higher-Order Functions & functools - Advanced Python Roadmap

"""
🔹 What are Higher-Order Functions?
- A higher-order function (HOF) is a function that:
  1. Accepts another function as an argument
  2. Returns a function as a result
- HOFs are used to **write cleaner, reusable, and functional-style code**.

Examples of built-in HOFs in Python: map(), filter(), reduce(), sorted(), max(), min()
"""

# -------------------------
# 1. Functions as Arguments
# -------------------------
def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

print(apply_function(square, 5))   # 25

# -------------------------
# 2. Functions Returning Functions
# -------------------------
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)
print(times3(10))  # 30

# -------------------------
# 3. Using map(), filter(), reduce()
# -------------------------
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# map → apply a function to each item
squared = list(map(lambda x: x**2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# filter → select items based on a condition
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # [2, 4]

# reduce → combine items into a single value
sum_all = reduce(lambda a, b: a + b, numbers)
print(sum_all)  # 15

# -------------------------
# 4. functools.lru_cache (Caching)
# -------------------------
from functools import lru_cache

@lru_cache(maxsize=32)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print([fibonacci(n) for n in range(10)])
# Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

# -------------------------
# 5. functools.partial (Fixing Arguments)
# -------------------------
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
cube = partial(power, exponent=3)

print(square(5))  # 25
print(cube(2))    # 8

# -------------------------
# ✅ Most Important Points to Remember
# -------------------------
"""
1. Higher-Order Functions (HOF) = functions that accept/return functions.
2. map(func, iterable) → apply func to all items.
3. filter(func, iterable) → filter items based on func.
4. reduce(func, iterable) → reduce iterable to a single value.
5. functools.lru_cache → caches function results for performance.
6. functools.partial → fixes some arguments of a function for reusability.
7. HOFs make your code **clean, reusable, and memory-efficient**.
"""
