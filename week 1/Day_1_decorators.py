from functools import wraps  # Helps preserve metadata of the original function

# 🎯 Step 1: Define a decorator function
def log_decorator(func):
    """
    A decorator that logs the function call details: name, arguments, and return value.
    """
    @wraps(func)  # Preserves the original function's name and docstring
    def wrapper(*args, **kwargs):
        # Before calling the original function
        print(f"[LOG] Calling '{func.__name__}' with arguments: {args} and keyword arguments: {kwargs}")
        
        # Call the original function and store the result
        result = func(*args, **kwargs)
        
        # After the function call
        print(f"[LOG] '{func.__name__}' returned: {result}")
        
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

# 🧪 Step 2: Use the decorator with a sample function
@log_decorator  # This applies the decorator to the function below
def add(a, b):
    """
    Returns the sum of two numbers.
    """
    return a + b

@log_decorator
def greet(name):
    """
    Returns a greeting message for the given name.
    """
    return f"Hello, {name}!"

# 🚀 Step 3: Call the decorated functions
add(10, 5)
greet("Priya")