import math
import random

def slowfun(x, y, cache={}):
    # TODO: Modify to produce the same results, but much faster
    
    v = x, y 
    
    if v not in cache:
        cache[v] = math.pow(v[0], v[1])
    if v not in cache:
        cache[v] = math.factorial(v)
    if v not in cache:   
        cache[v] //= (x + y)
    if v not in cache:
        cache[v] %= 982451653
        

    return cache[v]


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
