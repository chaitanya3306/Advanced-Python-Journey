# def uppercase(func):
#     def wrapper(*args, **kwargs):
#         print(f"Making it Uppercase ({func(*args, **kwargs)})")
#         result=func(*args, **kwargs)
#         print("Uppercased!!")
#         return result.upper()
    
#     return wrapper

# @uppercase
# def greet(name):
#     return f'hello {name} !!'

# name='Chaitanya'

# print(greet(name))

import random
def retry(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempts in range(1,n+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"attempt {attempts} Faliled : {e}")
                    if attempts==n:
                        print("attempts over")
                        break
        return wrapper
    return decorator

@retry(3)
def unstable():
    if random.choice([True,False]):
        raise ValueError('Random Failure')
    return 'Success !!'

print(unstable())