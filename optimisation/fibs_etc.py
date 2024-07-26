def fib(n, deepth=0, cache=None):
    if cache is None:
        cache = {}
    if n == 0 or n == 1:
        return 1
    else:
        if n in cache:
            return cache[n]
        
        cache[n] = fib(n-1, deepth=deepth+1, cache=cache) + fib(n-2, deepth=deepth+1, cache=cache)
        
        print(deepth * " " + ">", n, cache[n])

        return cache[n]
    

print(fib(10))