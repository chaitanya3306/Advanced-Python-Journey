# #1:
# nums=[1,2,3,4,5]

# operation=input('Enter operation (eg:square,cube) :')

# if 'sq' in operation:
#     print(list(map(lambda x:x**2,nums)))
# elif 'cu' in operation:
#     print(list(map(lambda x:x**3,nums)))
# else:
#     print('Invalid Input')
    

#2 factorial using lru_cache functool

from functools import lru_cache
import time
@lru_cache(maxsize=None)
def factorial(n):
    if n<=1:
        return 1
    return n*factorial(n-1)
start=time.time()
print([factorial(n) for n in range(10)])
end=time.time()
print(f"the function takes {(end-start):.4f} sec to run")
print(factorial.cache_info())