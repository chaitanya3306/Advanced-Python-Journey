# # #1:

# def process_numbers(numbers, operation):
#     # Define operations
#     operations = {
#         "square": lambda x: x**2,
#         "cube": lambda x: x**3,
#         "double": lambda x: x*2
#     }
    
#     if operation not in operations:
#         raise ValueError("Invalid operation! Use 'square', 'cube', or 'double'.")
    
#     # Step 1: Apply map
#     processed = map(operations[operation], numbers)
    
#     # Step 2: Filter out > 50
#     filtered = filter(lambda x: x <= 50, processed)
    
#     return list(filtered)


# # ✅ Test
# nums = [2, 4, 6, 8]
# print(process_numbers(nums, "square"))  # [4, 16, 36]
# print(process_numbers(nums, "cube"))    # [8, 64] → but 64 is > 50, so [8]
# print(process_numbers(nums, "double"))  # [4, 8, 12, 16]



# #2 factorial using lru_cache functool

# from functools import lru_cache
# import time

# @lru_cache(maxsize=None)   # Unlimited caching
# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     return n * factorial(n-1)


# # ✅ Measure performance
# start = time.time()
# print(factorial(1000))   # First call → slow
# print("First call time:", time.time() - start)

# start = time.time()
# print(factorial(1000))   # Second call → instant (cached)
# print("Second call time:", time.time() - start)





# 3 ✅ Compute factorial for a list of numbers (efficiently using caching)


from functools import partial
from datetime import datetime

# Generic logging function
def log(level, message):
    print(f"[{datetime.now()}] {level}: {message}")

# Pre-configured loggers using partial
info_log = partial(log, "INFO")
debug_log = partial(log, "DEBUG")
error_log = partial(log, "ERROR")


# Logging decorator
def logger(log_func):
    def decorator(func):
        def wrapper(*args, **kwargs):
            log_func(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            log_func(f"{func.__name__} returned {result}")
            return result
        return wrapper
    return decorator


# Example functions
@logger(info_log)
def add(a, b):
    return a + b

@logger(debug_log)
def multiply(a, b):
    return a * b


# ✅ Test
add(5, 3)
multiply(4, 6)
