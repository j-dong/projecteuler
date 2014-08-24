import math

def sigma(n):
    r = 2
    # do 2 first
    while n & 1 == 0:
        n = n >> 1
        r = r << 1
    r -= 1
    # find factors, similar to #3
    # very similar to #12
    fac = 3
    maxf = math.sqrt(n)
    while n > 1 and fac <= maxf:
        exp = 0
        while n % fac == 0:
            n = n // fac
            exp += 1
        if exp > 0:
            maxf = math.sqrt(n)
            r *= (fac ** (exp + 1) - 1) // (fac - 1)
        fac += 2
    if n != 1:
        r *= (n * n - 1) // (n - 1)
    return r

def tau(n):
    r = 1
    # do 2 first
    while n & 1 == 0:
        n = n >> 1
        r += 1
    # find factors, similar to #3
    fac = 3
    maxf = math.sqrt(n)
    while n > 1 and fac <= maxf:
        exp = 0
        while n % fac == 0:
            n = n / fac
            exp += 1
        if exp > 0:
            maxf = math.sqrt(n)
            r *= (exp + 1)
        fac += 2
    if n != 1:
        r *= 2
    return r

def fib(a = 0, b = 1):
    while True:
        yield a
        b += a
        a = b - a

def nth(seq, n, default = None):
    import itertools
    return next(itertools.islice(seq, n, None), default)
